from sqlalchemy import Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from database.models.declarative_base import Base
from sqlalchemy import types


class Metadata(Base):
    __tablename__ = "metadata"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=False)
    round: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[Optional[str]] = mapped_column(String(13), nullable=True)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    fk_metadata_league: Mapped["Leagues"] = relationship(back_populates="metadata_league_fk")