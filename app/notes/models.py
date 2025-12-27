from sqlalchemy.orm import (
Mapped,
mapped_column,
)
from sqlalchemy import (
select,
String,
Text
)
from app.db.base import Base


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)