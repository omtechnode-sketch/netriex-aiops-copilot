from fastapi import APIRouter
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.protected import router as protected_router
from app.api.v1.endpoints.incidents import router as incident_router
from app.api.v1.endpoints.logs import router as logs_router


router = APIRouter()

router.include_router(auth_router)
router.include_router(protected_router)
router.include_router(incident_router)
router.include_router(logs_router)

@router.get("/ping")
def ping():
    return {"message": "pong"}
