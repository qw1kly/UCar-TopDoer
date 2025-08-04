from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from pydantic import BaseModel


class Base(DeclarativeBase):
    pass

class Comment(Base):
    __tablename__ = 'otz'

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(255))
    sentiment: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[str] = mapped_column(String(255))

class QueryModel(BaseModel):

    text: str