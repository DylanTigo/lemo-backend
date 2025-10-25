from typing import List
from fastapi import Depends
from src.repositories.category_repo import CategoryRepository
from src.database import Database, get_db
from src.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryOut,
    CategoryWithChildren,
    CategoryListOut,
)
from src.utils.exceptions import NotFoundException


class CategoryService:
    def __init__(self, db: Database):
        self.db = db
        self.repo = CategoryRepository(db)

    async def get_category(self, category_id: int) -> CategoryOut:
        """Récupère une catégorie"""
        category = await self.repo.get_by_id(category_id)
        if not category:
            raise NotFoundException(f"Catégorie {category_id} non trouvée")
        return CategoryOut.model_validate(category)

    async def get_category_with_children(
        self, category_id: int
    ) -> CategoryWithChildren:
        """Récupère une catégorie avec ses sous-catégories"""
        category = await self.repo.get_with_children(category_id)
        if not category:
            raise NotFoundException(f"Catégorie {category_id} non trouvée")
        return CategoryWithChildren.model_validate(category)

    async def list_categories(self, root_only: bool = False) -> CategoryListOut:
        """Liste les catégories"""
        if root_only:
            categories = await self.repo.list_root_categories()
        else:
            categories = await self.repo.list_all()

        total = await self.repo.get_count()
        categories_out = [CategoryOut.model_validate(c) for c in categories]

        return CategoryListOut(categories=categories_out, total=total)

    async def create_category(self, category_data: CategoryCreate) -> CategoryOut:
        """Crée une catégorie (Admin)"""
        # Vérifier si le parent existe
        if category_data.parent_id:
            parent = await self.repo.get_by_id(category_data.parent_id)
            if not parent:
                raise NotFoundException(
                    f"Catégorie parent {category_data.parent_id} non trouvée"
                )
        existing_category = await self.repo.get_by_name(category_data.name)
        if existing_category:
            raise ValueError(
                f"Une catégorie avec le nom '{category_data.name}' existe déjà"
            )
        category = await self.repo.create(category_data.model_dump())
        return CategoryOut.model_validate(category)

    async def update_category(
        self, category_id: int, category_data: CategoryUpdate
    ) -> CategoryOut:
        """Met à jour une catégorie (Admin)"""
        update_data = category_data.model_dump(exclude_unset=True)

        # Vérifier si le nouveau parent existe
        if "parent_id" in update_data and update_data["parent_id"]:
            if update_data["parent_id"] == category_id:
                raise ValueError("Une catégorie ne peut pas être son propre parent")
            parent = await self.repo.get_by_id(update_data["parent_id"])
            if not parent:
                raise NotFoundException(
                    f"Catégorie parent {update_data['parent_id']} non trouvée"
                )

        category = await self.repo.update(category_id, update_data)
        if not category:
            raise NotFoundException(f"Catégorie {category_id} non trouvée")

        return CategoryOut.model_validate(category)

    async def delete_category(self, category_id: int) -> dict:
        """Supprime une catégorie (Admin)"""
        deleted = await self.repo.delete(category_id)
        if not deleted:
            raise NotFoundException(f"Catégorie {category_id} non trouvée")

        return {"message": f"Catégorie {category_id} supprimée avec succès"}


def get_category_service(db: Database = Depends(get_db)) -> CategoryService:
    return CategoryService(db)
