import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import db
from src.models.users import User
from src.schemas.enum import UserRole
from src.utils.security import hash_password


async def create_admin():
    async with db.get_session() as session:
        from sqlalchemy import select

        result = await session.execute(select(User).where(User.email == "dylan@admin.com"))
        existing_admin = result.scalar_one_or_none()

        if existing_admin:
            print("❌ L'admin existe déjà !")
            return

        # Créer l'admin
        admin = User(
            name="Admin Dylan",
            email="dylan@admin.com",
            password=hash_password("admin123"),
            role=UserRole.ADMIN,
        )

        session.add(admin)
        await session.commit()
        await session.refresh(admin)

        print("✅ Admin créé avec succès !")
        print(f"   Email: {admin.email}")
        print(f"   Password: admin123")
        print(f"   ID: {admin.id}")


if __name__ == "__main__":
    asyncio.run(create_admin())
