from typing import Optional, List
from fastapi import Depends
from src.repositories.product_repo import ProductRepository
from src.repositories.brand_repo import BrandRepository
from src.repositories.category_repo import CategoryRepository
from src.repositories.attribute_repo import AttributeRepository
from src.database import Database, get_db
from src.schemas.cart import CartProductOut, CartRequest, CartResponse
from src.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductOut,
    ProductListOut,
    PromoUpdate,
)
from src.utils.exceptions import NotFoundException


class ProductService:
    def __init__(self, db: Database):
        self.db = db
        self.product_repo = ProductRepository(db)
        self.brand_repo = BrandRepository(db)
        self.category_repo = CategoryRepository(db)
        self.attribute_repo = AttributeRepository(db)

    def _generate_product_name(
        self, category_name: str, brand_name: str, attributes: List[dict]
    ) -> str:
        """Génère le nom générique du produit"""
        # Format: Catégorie + Marque + Attributs
        parts = [category_name, brand_name]

        # Ajouter les valeurs des attributs
        for attr in attributes:
            parts.append(attr["value"])

        return " ".join(parts)

    async def get_product(self, product_id: str) -> ProductOut:
        """Récupère un produit par ID"""
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise NotFoundException(f"Produit {product_id} non trouvé")
        return ProductOut.model_validate(product)

    async def list_products(
        self,
        page: int = 1,
        page_size: int = 20,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        condition: Optional[int] = None,
        is_new: Optional[bool] = None,
        latest_products: Optional[bool] = False,
        latest_products_count: Optional[int] = 6,
    ) -> ProductListOut:
        """Liste les produits avec filtres"""
        skip = (page - 1) * page_size

        products, total = await self.product_repo.list_products(
            skip=skip,
            limit=page_size,
            search=search,
            category_id=category_id,
            brand_id=brand_id,
            min_price=min_price,
            max_price=max_price,
            condition=condition,
            is_new=is_new,
            latest_products=latest_products,
            latest_products_count=latest_products_count,
        )

        products_out = [ProductOut.model_validate(p) for p in products]
        has_more = skip + len(products) < total

        return ProductListOut(
            products=products_out, total=total, page=page, page_size=page_size, has_more=has_more
        )

    async def create_product(self, product_data: ProductCreate) -> ProductOut:
        """Crée un produit avec validation des relations (Admin)"""
        # 1. Vérifier que la marque existe
        brand = await self.brand_repo.get_by_id(product_data.brand_id)
        if not brand:
            raise NotFoundException(f"Marque {product_data.brand_id} non trouvée")

        # 2. Vérifier que la catégorie existe
        category = await self.category_repo.get_by_id(product_data.category_id)
        if not category:
            raise NotFoundException(f"Catégorie {product_data.category_id} non trouvée")

        # 3. Vérifier que tous les attributs existent
        attribute_values = []
        for attr in product_data.attributes:
            attribute = await self.attribute_repo.get_by_id(attr.attribute_id)
            if not attribute:
                raise NotFoundException(f"Attribut {attr.attribute_id} non trouvé")
            attribute_values.append(
                {
                    "attribute_id": attr.attribute_id,
                    "value": attr.value,
                    "name": attribute.name,  # Pour générer le nom
                }
            )

        # 4. Générer le nom générique
        product_name = self._generate_product_name(
            category.name, brand.name, attribute_values
        )

        # 5. Créer le produit
        product_dict = product_data.model_dump(exclude={"image_urls", "attributes"})
        product_dict["name"] = product_name

        product = await self.product_repo.create_product(product_dict)

        # 6. Ajouter les images
        if product_data.image_urls:
            await self.product_repo.add_product_images(
                product.id, product_data.image_urls
            )

        # 7. Ajouter les attributs
        if attribute_values:
            await self.product_repo.add_product_attributes(product.id, attribute_values)

        # 8. Recharger le produit avec toutes les relations
        product = await self.product_repo.get_by_id(product.id)
        return ProductOut.model_validate(product)

    async def update_product(
        self, product_id: str, product_data: ProductUpdate
    ) -> ProductOut:
        """Met à jour un produit (Admin)"""
        # Vérifier que le produit existe
        existing_product = await self.product_repo.get_by_id(product_id)
        if not existing_product:
            raise NotFoundException(f"Produit {product_id} non trouvé")

        update_data = product_data.model_dump(
            exclude_unset=True, exclude={"image_urls", "attributes"}
        )

        # Vérifier les nouvelles relations si fournies
        if product_data.brand_id is not None:
            brand = await self.brand_repo.get_by_id(product_data.brand_id)
            if not brand:
                raise NotFoundException(f"Marque {product_data.brand_id} non trouvée")

        if product_data.category_id is not None:
            category = await self.category_repo.get_by_id(product_data.category_id)
            if not category:
                raise NotFoundException(
                    f"Catégorie {product_data.category_id} non trouvée"
                )

        # Régénérer le nom si marque/catégorie/attributs changent
        should_regenerate_name = (
            product_data.brand_id is not None
            or product_data.category_id is not None
            or product_data.attributes is not None
        )

        if should_regenerate_name:
            # Récupérer les données actuelles ou nouvelles
            brand_id = (
                product_data.brand_id
                if product_data.brand_id is not None
                else existing_product.brand_id
            )
            category_id = (
                product_data.category_id
                if product_data.category_id is not None
                else existing_product.category_id
            )

            brand = await self.brand_repo.get_by_id(brand_id)
            category = await self.category_repo.get_by_id(category_id)

            # Gérer les attributs
            if product_data.attributes is not None:
                attribute_values = []
                for attr in product_data.attributes:
                    attribute = await self.attribute_repo.get_by_id(attr.attribute_id)
                    if not attribute:
                        raise NotFoundException(
                            f"Attribut {attr.attribute_id} non trouvé"
                        )
                    attribute_values.append(
                        {
                            "attribute_id": attr.attribute_id,
                            "value": attr.value,
                            "name": attribute.name,
                        }
                    )
            else:
                # Garder les attributs existants pour le nom
                attribute_values = [{"value": ""} for _ in existing_product.attributes]

            update_data["name"] = self._generate_product_name(
                category.name, brand.name, attribute_values
            )

        # Mettre à jour le produit
        product = await self.product_repo.update_product(product_id, update_data)

        # Mettre à jour les images si fournies
        if product_data.image_urls is not None:
            await self.product_repo.delete_product_images(product_id)
            if product_data.image_urls:
                await self.product_repo.add_product_images(
                    product_id, product_data.image_urls
                )

        # Mettre à jour les attributs si fournis
        if product_data.attributes is not None:
            await self.product_repo.delete_product_attributes(product_id)
            if product_data.attributes:
                attrs_data = [
                    {"attribute_id": attr.attribute_id, "value": attr.value}
                    for attr in product_data.attributes
                ]
                await self.product_repo.add_product_attributes(product_id, attrs_data)

        # Recharger le produit
        product = await self.product_repo.get_by_id(product_id)
        return ProductOut.model_validate(product)

    async def delete_product(self, product_id: str) -> dict:
        """Supprime un produit (Admin)"""
        deleted = await self.product_repo.delete_product(product_id)

        if not deleted:
            raise NotFoundException(f"Produit {product_id} non trouvé")

        return {"message": f"Produit {product_id} supprimé avec succès"}

    async def list_featured_products(self, limit: int = 10) -> List[ProductOut]:
        """Liste les produits en vedette (Public)"""
        products = await self.product_repo.list_featured_products(limit)
        return [ProductOut.model_validate(p) for p in products]

    async def list_daily_promos(self) -> List[ProductOut]:
        """Liste les promotions du jour actives (Public)"""
        products = await self.product_repo.list_daily_promos()
        return [ProductOut.model_validate(p) for p in products] or []

    async def update_product_promo(
        self, product_id: str, promo_data: PromoUpdate
    ) -> ProductOut:
        """Met à jour la promotion d'un produit (Admin)"""
        # Vérifier que le produit existe
        existing_product = await self.product_repo.get_by_id(product_id)
        if not existing_product:
            raise NotFoundException(f"Produit {product_id} non trouvé")

        # Validation : si promo active, pourcentage et dates requis
        if promo_data.is_daily_promo:
            if not promo_data.promo_percentage:
                raise ValueError(
                    "Le pourcentage de réduction est requis pour activer une promotion"
                )
            if not promo_data.promo_start_date or not promo_data.promo_end_date:
                raise ValueError(
                    "Les dates de début et fin sont requises pour une promotion"
                )
            if promo_data.promo_percentage < 1 or promo_data.promo_percentage > 99:
                raise ValueError(
                    "Le pourcentage de réduction doit être entre 1% et 99%"
                )

        promo_dict = promo_data.model_dump()
        product = await self.product_repo.update_promo(product_id, promo_dict)

        return ProductOut.model_validate(product)

    async def get_cart_products(self, cart_request: CartRequest) -> CartResponse:
        """Récupère les produits du panier (Public)"""
        # Récupérer les produits
        products = await self.product_repo.get_products_by_ids(cart_request.product_ids)

        # Construire la réponse avec disponibilité
        cart_products = []
        unavailable_count = 0

        for product in products:
            is_available = product.stock_quantity > 0
            if not is_available:
                unavailable_count += 1

            cart_products.append(
                CartProductOut(
                    product=ProductOut.model_validate(product),
                    is_available=is_available,
                    stock_quantity=product.stock_quantity,
                )
            )

        return CartResponse(
            products=cart_products,
            total_products=len(cart_products),
            unavailable_count=unavailable_count,
        )


def get_product_service(db: Database = Depends(get_db)) -> ProductService:
    return ProductService(db)
