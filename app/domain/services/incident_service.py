from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models import Incident

from app.infrastructure.queue.queue import event_queue
from app.workers.incident_worker import process_incident

class IncidentService:

    async def create_incident(self, db: AsyncSession, payload, tenant_id: int):
        incident = Incident(
            title=payload.title,
            description=payload.description,
            severity=payload.severity,
            tenant_id=tenant_id
        )
        db.add(incident)
        await db.commit()
        await db.refresh(incident)

        event_queue.enqueue(process_incident, incident.id)

        return incident

