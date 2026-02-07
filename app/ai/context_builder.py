from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.domain.models import LogEntry, Incident

async def build_context(db: AsyncSession, incident_id: int):
    result = await db.execute(
        select(Incident).where(Incident.id == incident_id)
    )
    incident = result.scalar_one()

    logs = await db.execute(
        select(LogEntry).where(LogEntry.tenant_id == incident.tenant_id)
    )

    logs_text = "\n".join(
        [f"{l.service} [{l.level}]: {l.message}" for l in logs.scalars().all()]
    )

    context = f"""
INCIDENT:
Title: {incident.title}
Description: {incident.description}
Severity: {incident.severity}

RECENT LOGS:
{logs_text}
"""

    return context
