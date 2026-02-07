from fastapi import APIRouter, Depends
from app.api.deps import get_current_user
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

router = APIRouter(prefix="/protected", tags=["Protected"])

@router.get("/me")
async def read_me(user=Depends(get_current_user), credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials 
    return {"user": user, 'token': token}
