from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db
from app.domain.schemas.incident import IncidentCreate, IncidentResponse
from app.domain.services.incident_service import IncidentService
from app.api.deps import get_current_user

router = APIRouter(prefix="/incidents", tags=["Incidents"])

service = IncidentService()

@router.post("/", response_model=IncidentResponse)
async def create_incident(
    payload: IncidentCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    return await service.create_incident(db, payload, tenant_id=user["tenant_id"])
