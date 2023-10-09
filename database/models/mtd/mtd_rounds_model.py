from sqlalchemy import Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from database.models.declarative_base import Base
from sqlalchemy import types

class RoundsMetadata(Base):
    __tablename__ = "rounds"
    __table_args__ = {"schema": "mtd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_league_mtd: Mapped[int] = mapped_column(ForeignKey("mtd.leagues.id"), nullable=False)
    round: Mapped[int] = mapped_column(Integer, nullable=False)
    played: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    metadata_league_round_fk: Mapped[List["LeaguesMetadata"]] = relationship(back_populates="fk_metadata_rounds")