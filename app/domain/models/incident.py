from sqlalchemy import String, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum as PyEnum
from app.infrastructure.db.base import Base

class IncidentStatus(PyEnum):
    detected = "detected"
    analyzing = "analyzing"
    mitigating = "mitigating"
    resolved = "resolved"
    closed = "closed"

class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    severity: Mapped[str] = mapped_column(String(50))
    status: Mapped[IncidentStatus] = mapped_column(Enum(IncidentStatus), default=IncidentStatus.detected)

    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"))
