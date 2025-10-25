from typing import List
from fastapi import Depends
from src.repositories.attribute_repo import AttributeRepository
from src.database import Database, get_db
from src.schemas.attribute import (
    AttributeCreate,
    AttributeUpdate,
    AttributeOut,
    AttributeListOut,
)
from src.utils.exceptions import NotFoundException


class AttributeService:
    def __init__(self, db: Database):
        self.db = db
        self.repo = AttributeRepository(db)

    async def get_attribute(self, attribute_id: int) -> AttributeOut:
        """Récupère un attribut"""
        attribute = await self.repo.get_by_id(attribute_id)
        if not attribute:
            raise NotFoundException(f"Attribut {attribute_id} non trouvé")
        return AttributeOut.model_validate(attribute)

    async def list_attributes(self) -> AttributeListOut:
        """Liste les attributs"""
        attributes = await self.repo.list_all()
        total = await self.repo.get_count()
        attributes_out = [AttributeOut.model_validate(a) for a in attributes]

        return AttributeListOut(attributes=attributes_out, total=total)

    async def create_attribute(self, attribute_data: AttributeCreate) -> AttributeOut:
        """Crée un attribut (Admin)"""
        attribute = await self.repo.create(attribute_data.model_dump())
        if not attribute:
            raise NotFoundException(
                f"Attribut avec le nom '{attribute_data.name}' existe déjà"
            )
        return AttributeOut.model_validate(attribute)

    async def update_attribute(
        self, attribute_id: int, attribute_data: AttributeUpdate
    ) -> AttributeOut:
        """Met à jour un attribut (Admin)"""
        update_data = attribute_data.model_dump(exclude_unset=True)
        attribute = await self.repo.update(attribute_id, update_data)

        if not attribute:
            raise NotFoundException(f"Attribut {attribute_id} non trouvé")

        return AttributeOut.model_validate(attribute)

    async def delete_attribute(self, attribute_id: int) -> dict:
        """Supprime un attribut (Admin)"""
        deleted = await self.repo.delete(attribute_id)
        if not deleted:
            raise NotFoundException(f"Attribut {attribute_id} non trouvé")

        return {"message": f"Attribut {attribute_id} supprimé avec succès"}


def get_attribute_service(db: Database = Depends(get_db)) -> AttributeService:
    return AttributeService(db)
