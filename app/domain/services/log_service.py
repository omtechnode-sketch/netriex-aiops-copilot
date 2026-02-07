from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models import LogEntry

class LogService:

    async def ingest_log(self, db: AsyncSession, payload, tenant_id: int):
        log = LogEntry(
            service=payload.service,
            level=payload.level,
            message=payload.message,
            tenant_id=tenant_id
        )
        db.add(log)
        await db.commit()
        return log
