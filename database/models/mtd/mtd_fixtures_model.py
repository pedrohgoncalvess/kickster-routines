from sqlalchemy import Integer, String, ForeignKey, func, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from database.models.declarative_base import Base
from sqlalchemy import types

class FixturesMetadata(Base):
    __tablename__ = "fixtures"
    __table_args__ = {"schema": "mtd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    stats_metadata: Mapped[str] = mapped_column(String(13), nullable=False)
    lineups_metadata: Mapped[str] = mapped_column(String(13), nullable=False)
    events_metadata: Mapped[str] = mapped_column(String(13), nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    fk_metadata_fixture: Mapped["Fixtures"] = relationship(back_populates="metadata_fixture_fk")