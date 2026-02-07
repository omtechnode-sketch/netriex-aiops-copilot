from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.db.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str] = mapped_column(String(500), unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_revoked: Mapped[bool] = mapped_column(Boolean, default=False)
