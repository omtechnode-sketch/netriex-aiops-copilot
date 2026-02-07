from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.models import User, Tenant, RefreshToken
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token, create_refresh_token
from app.common.exceptions import AuthException

class AuthService:

    async def register(self, db: AsyncSession, email: str, password: str, tenant_name: str):
        tenant = Tenant(name=tenant_name, domain=tenant_name.lower())
        db.add(tenant)
        await db.flush()

        user = User(
            email=email,
            hashed_password=hash_password(password),
            tenant_id=tenant.id
        )
        db.add(user)
        await db.commit()

        return user

    async def login(self, db: AsyncSession, email: str, password: str):
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()

        if not user or not verify_password(password, user.hashed_password):
            raise AuthException("Invalid credentials")

        payload = {
            "sub": str(user.id),
            "tenant_id": user.tenant_id,
        }

        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)

        db.add(RefreshToken(token=refresh_token, user_id=user.id))
        await db.commit()

        return access_token, refresh_token
