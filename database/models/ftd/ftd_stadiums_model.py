from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from database.models.declarative_base import Base

class Stadiums(Base):
    __tablename__ = "stadiums"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    stadium_team: Mapped[List["Teams"]] = relationship(back_populates="home_stadium")
    stadium_fixture: Mapped[List["Fixtures"]] = relationship(back_populates="fixture_stadium")

    name: Mapped[Optional[str]] = mapped_column(String(150), nullable=False, unique=True)
    state: Mapped[str] = mapped_column(String(40), nullable=False)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(250), nullable=False)
    capacity: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    surface: Mapped[Optional[str]] = mapped_column(String(30), nullable=False)
    image: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)