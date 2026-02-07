from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db
from app.domain.schemas.logs import LogIngest
from app.domain.services.log_service import LogService
from app.api.deps import get_current_user

router = APIRouter(prefix="/logs", tags=["Logs"])

service = LogService()

@router.post("/ingest")
async def ingest_log(
    payload: LogIngest,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    await service.ingest_log(db, payload, tenant_id=user["tenant_id"])
    return {"status": "ok"}
