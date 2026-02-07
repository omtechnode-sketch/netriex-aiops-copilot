import hashlib
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from app.api.deps import get_current_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
     # Pre-hash to remove bcrypt 72 byte limit
    prehashed = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(prehashed)

def verify_password(password: str, hashed: str) -> bool:
    prehashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.verify(prehashed, hashed)

def require_permission(permission: str):
    async def checker(user=Depends(get_current_user)):
        if permission not in user.get("permissions", []):
            raise HTTPException(status_code=403, detail="Permission denied")
    return checker
