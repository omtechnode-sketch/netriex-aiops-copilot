from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.base import Base

class LogEntry(Base):
    __tablename__ = "log_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    service: Mapped[str] = mapped_column(String(100))
    level: Mapped[str] = mapped_column(String(50))
    message: Mapped[str] = mapped_column(Text)

    tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"))
