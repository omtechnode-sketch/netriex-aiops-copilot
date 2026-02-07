from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db
from app.domain.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.domain.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

auth_service = AuthService()

@router.post("/register")
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)):
    user = await auth_service.register(
        db, payload.email, payload.password, payload.tenant_name
    )
    return {"id": user.id, "email": user.email}

@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    access, refresh = await auth_service.login(
        db, payload.email, payload.password
    )
    return TokenResponse(access_token=access, refresh_token=refresh)
