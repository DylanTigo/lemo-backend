from typing import Optional, List, Dict
from sqlalchemy import select, func, or_, delete, distinct
from sqlalchemy.orm import selectinload
from src.models.products import Product
from src.models.product_images import ProductImage
from src.models.categories import Category
from src.models.brands import Brand
from src.models.attributes import Attribute
from src.models.associations import ProductAttribute
from src.repositories.base import BaseRepository
from src.utils.logging_config import logger


class ProductRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Product)

    async def _get_category_with_children_ids(self, category_id: int) -> List[int]:
        """Récupère récursivement tous les IDs d'une catégorie et de ses enfants"""
        async with self.db.get_session() as session:
            category_ids = [category_id]
            
            # Récupérer la catégorie avec ses sous-catégories
            query = select(Category).options(
                selectinload(Category.subcategories)
            ).where(Category.id == category_id)
            
            result = await session.execute(query)
            category = result.scalar_one_or_none()
            
            if not category:
                return category_ids
            
            # Fonction récursive pour obtenir tous les enfants
            async def get_all_subcategories(cat_id: int) -> List[int]:
                query = select(Category).where(Category.parent_id == cat_id)
                result = await session.execute(query)
                subcategories = result.scalars().all()
                
                ids = []
                for subcat in subcategories:
                    ids.append(subcat.id)
                    # Récursion pour les sous-catégories de niveau inférieur
                    child_ids = await get_all_subcategories(subcat.id)
                    ids.extend(child_ids)
                
                return ids
            
            # Obtenir tous les IDs des sous-catégories
            subcategory_ids = await get_all_subcategories(category_id)
            category_ids.extend(subcategory_ids)
            
            return category_ids

    async def get_by_id(self, product_id: str) -> Optional[Product]:
        """Récupère un produit par ID avec toutes ses relations"""
        async with self.db.get_session() as session:
            query = (
                select(Product)
                .options(
                    selectinload(Product.images),
                    selectinload(Product.brand),
                    selectinload(Product.category),
                    selectinload(Product.product_attributes).selectinload(ProductAttribute.attribute),
                )
                .where(Product.id == product_id)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def list_products(
        self,
        skip: int,
        limit: int,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        condition: Optional[int] = None,
        is_new: Optional[bool] = None,
        latest_products: Optional[bool] = False,
        latest_products_count: Optional[int] = 6,
    ) -> tuple[List[Product], int]:
        """Liste les produits avec filtres et pagination"""
        async with self.db.get_session() as session:
            query = select(Product).options(
                selectinload(Product.images),
                selectinload(Product.brand),
                selectinload(Product.category),
                selectinload(Product.product_attributes).selectinload(ProductAttribute.attribute),
            )

            # Filtre recherche textuelle (sur le nom générique indexé)
            if search:
                query = query.where(
                    or_(
                        Product.name.ilike(f"%{search}%"),
                        Product.description.ilike(f"%{search}%"),
                    )
                )

            # Filtres
            if category_id:
                # Récupérer la catégorie et toutes ses sous-catégories
                category_ids = await self._get_category_with_children_ids(category_id)
                query = query.where(Product.category_id.in_(category_ids))

            if brand_id:
                query = query.where(Product.brand_id == brand_id)

            if min_price is not None:
                query = query.where(Product.price >= min_price)

            if max_price is not None:
                query = query.where(Product.price <= max_price)

            if latest_products:
                query = query.where(
                    Product.id.in_(
                        select(Product.id)
                        .order_by(Product.created_at.desc())
                        .limit(latest_products_count)
                    )
                )

            if is_new is not None:
                if is_new:
                    query = query.where(Product.condition.is_(None))
                else:
                    query = query.where(Product.condition.isnot(None))
            elif condition is not None:
                query = query.where(Product.condition == condition)

            # Compte total
            count_query = select(func.count()).select_from(query.subquery())
            total = await session.scalar(count_query)

            # Pagination
            query = query.offset(skip).limit(limit).order_by(Product.created_at.desc())

            result = await session.execute(query)
            products = result.scalars().all()

            return products, total

    async def get_available_filters(
        self,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        condition: Optional[int] = None,
        is_new: Optional[bool] = None,
    ) -> Dict:
        """Calcule les filtres disponibles basés sur les critères de recherche actuels"""
        async with self.db.get_session() as session:
            # Construire la requête de base (sans les filtres qu'on veut analyser)
            base_query = select(Product)

            # Filtre recherche textuelle
            if search:
                base_query = base_query.where(
                    or_(
                        Product.name.ilike(f"%{search}%"),
                        Product.description.ilike(f"%{search}%"),
                    )
                )

            # Appliquer les filtres existants pour affiner les résultats
            if category_id:
                category_ids = await self._get_category_with_children_ids(category_id)
                base_query = base_query.where(Product.category_id.in_(category_ids))

            if brand_id:
                base_query = base_query.where(Product.brand_id == brand_id)

            if min_price is not None:
                base_query = base_query.where(Product.price >= min_price)

            if max_price is not None:
                base_query = base_query.where(Product.price <= max_price)

            if is_new is not None:
                if is_new:
                    base_query = base_query.where(Product.condition.is_(None))
                else:
                    base_query = base_query.where(Product.condition.isnot(None))
            elif condition is not None:
                base_query = base_query.where(Product.condition == condition)

            # 1. Calculer la plage de prix
            price_query = select(
                func.min(Product.price).label("min_price"),
                func.max(Product.price).label("max_price"),
            ).select_from(base_query.subquery())
            
            price_result = await session.execute(price_query)
            price_row = price_result.first()
            
            price_range = None
            if price_row and price_row.min_price is not None:
                price_range = {
                    "min_price": float(price_row.min_price),
                    "max_price": float(price_row.max_price),
                }

            # 2. Calculer les marques disponibles avec leur nombre
            filtered_products = base_query.subquery().alias("filtered_products")
            brands_query = (
                select(
                    Brand.id,
                    Brand.name,
                    func.count(filtered_products.c.id).label("count")
                )
                .select_from(filtered_products)
                .join(Brand, Brand.id == filtered_products.c.brand_id)
                .group_by(Brand.id, Brand.name)
                .order_by(func.count(filtered_products.c.id).desc())
            )

            brands_result = await session.execute(brands_query)
            brands = [
                {"brand_id": row.id, "brand_name": row.name, "count": row.count}
                for row in brands_result
            ]

            # 3. Calculer les catégories disponibles avec leur nombre
            filtered_products_cat = base_query.subquery().alias("filtered_products_cat")
            categories_query = (
                select(
                    Category.id,
                    Category.name,
                    func.count(filtered_products_cat.c.id).label("count")
                )
                .select_from(filtered_products_cat)
                .join(Category, Category.id == filtered_products_cat.c.category_id)
                .group_by(Category.id, Category.name)
                .order_by(func.count(filtered_products_cat.c.id).desc())
            )

            categories_result = await session.execute(categories_query)
            categories = [
                {"category_id": row.id, "category_name": row.name, "count": row.count}
                for row in categories_result
            ]

            # 4. Calculer les attributs disponibles avec leurs valeurs
            # D'abord, récupérer les product_ids filtrés
            product_ids_query = select(Product.id).select_from(base_query.subquery())
            product_ids_result = await session.execute(product_ids_query)
            product_ids = [row[0] for row in product_ids_result]

            attributes_data = {}
            if product_ids:
                # Récupérer tous les attributs avec leurs valeurs pour ces produits
                attrs_query = (
                    select(
                        Attribute.id,
                        Attribute.name,
                        Attribute.type,
                        ProductAttribute.value,
                        func.count(ProductAttribute.product_id).label("count")
                    )
                    .select_from(ProductAttribute)
                    .join(Attribute, Attribute.id == ProductAttribute.attribute_id)
                    .where(ProductAttribute.product_id.in_(product_ids))
                    .group_by(Attribute.id, Attribute.name, Attribute.type, ProductAttribute.value)
                    .order_by(Attribute.name, func.count(ProductAttribute.product_id).desc())
                )
                
                attrs_result = await session.execute(attrs_query)
                
                for row in attrs_result:
                    attr_id = row.id
                    attr_name = row.name
                    attr_type = row.type
                    value = row.value
                    count = row.count
                    
                    if attr_id not in attributes_data:
                        attributes_data[attr_id] = {
                            "attribute_id": attr_id,
                            "attribute_name": attr_name,
                            "attribute_type": attr_type,
                            "values": []
                        }
                    
                    attributes_data[attr_id]["values"].append({
                        "value": value,
                        "count": count
                    })

            attributes = list(attributes_data.values())

            return {
                "price_range": price_range,
                "brands": brands,
                "categories": categories,
                "attributes": attributes,
            }

    async def create_product(self, product_data: dict) -> Product:
        """Crée un produit"""
        async with self.db.get_session() as session:
            name =  product_data.get("name", "")
            # Assurer l'unicité du nom
            existing_product = await session.execute(
                select(Product).where(Product.name == name)
            )
            if existing_product.scalar_one_or_none(): 
                return None
            product = Product(**product_data)
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return product

    async def add_product_images(self, product_id: str, image_urls: List[str]):
        """Ajoute des images à un produit"""
        async with self.db.get_session() as session:
            for idx, url in enumerate(image_urls):
                image = ProductImage(
                    product_id=product_id, url=url, is_primary=True if idx == 0 else False
                )
                session.add(image)
            await session.commit()

    async def add_product_attributes(
        self, product_id: str, attributes: List[Dict[str, any]]
    ):
        """Ajoute des attributs avec leurs valeurs à un produit"""
        async with self.db.get_session() as session:
            for attr in attributes:
                product_attr = ProductAttribute(
                    product_id=product_id,
                    attribute_id=attr["attribute_id"],
                    value=attr["value"],
                )
                session.add(product_attr)
            await session.commit()

    async def update_product(
        self, product_id: str, product_data: dict
    ) -> Optional[Product]:
        """Met à jour un produit"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Product).where(Product.id == product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                return None

            for key, value in product_data.items():
                if value is not None:
                    setattr(product, key, value)

            await session.commit()
            await session.refresh(product)
            return product

    async def delete_product_images(self, product_id: str):
        """Supprime toutes les images d'un produit"""
        async with self.db.get_session() as session:
            await session.execute(
                delete(ProductImage).where(ProductImage.product_id == product_id)
            )
            await session.commit()

    async def delete_product_attributes(self, product_id: str):
        """Supprime tous les attributs d'un produit"""
        async with self.db.get_session() as session:
            await session.execute(
                delete(ProductAttribute).where(
                    ProductAttribute.product_id == product_id
                )
            )
            await session.commit()

    async def delete_product(self, product_id: str) -> bool:
        """Supprime un produit (cascade sur images et attributs)"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Product).where(Product.id == product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                return False

            await session.delete(product)
            await session.commit()
            return True

    async def list_featured_products(self, limit: int = 10) -> List[Product]:
        """Liste les produits en vedette"""
        async with self.db.get_session() as session:
            query = (
                select(Product)
                .options(
                    selectinload(Product.images),
                    selectinload(Product.brand),
                    selectinload(Product.category),
                    selectinload(Product.product_attributes).selectinload(ProductAttribute.attribute),
                )
                .where(Product.is_featured == True)
                .where(Product.stock_quantity > 0)
                .order_by(Product.created_at.desc())
                .limit(limit)
            )

            result = await session.execute(query)
            return result.scalars().all()

    async def list_daily_promos(self) -> List[Product]:
        """Liste les promotions du jour actives"""
        async with self.db.get_session() as session:
            now = func.now()

            query = (
                select(Product)
                .options(
                    selectinload(Product.images),
                    selectinload(Product.brand),
                    selectinload(Product.category),
                    selectinload(Product.product_attributes).selectinload(ProductAttribute.attribute),
                )
                .where(Product.is_daily_promo == True)
                .where(Product.promo_percentage.isnot(None))
                .where(Product.promo_start_date <= now)
                .where(Product.promo_end_date >= now)
                .where(Product.stock_quantity > 0)
                .order_by(
                    Product.promo_percentage.desc()
                )  # Trier par % de réduction décroissant
            )

            result = await session.execute(query)
            return result.scalars().all()

    async def update_promo(
        self, product_id: str, promo_data: dict
    ) -> Optional[Product]:
        """Met à jour les infos de promotion d'un produit"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Product).where(Product.id == product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                return None

            # Si on désactive la promo, réinitialiser les champs
            if not promo_data.get("is_daily_promo", True):
                product.is_daily_promo = False
                product.promo_percentage = None
                product.promo_start_date = None
                product.promo_end_date = None
            else:
                for key, value in promo_data.items():
                    setattr(product, key, value)

            await session.commit()
            await session.refresh(product)
            return product

    async def get_products_by_ids(self, product_ids: List[str]) -> List[Product]:
        """Récupère plusieurs produits par leurs IDs"""
        async with self.db.get_session() as session:
            query = (
                select(Product)
                .options(
                    selectinload(Product.images),
                    selectinload(Product.brand),
                    selectinload(Product.category),
                    selectinload(Product.product_attributes).selectinload(ProductAttribute.attribute),
                )
                .where(Product.id.in_(product_ids))
            )
            result = await session.execute(query)
            return result.scalars().all()
