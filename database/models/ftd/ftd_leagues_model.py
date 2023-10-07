from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from database.models.declarative_base import Base
from database.models.players_model import PlayersStats
from database.models.teams_model import TeamsFixturesStats
from database.models.teams_model import TeamsCardsStats
from database.models.teams_model import TeamsGoalsStats


class Leagues(Base):
    __tablename__ = "leagues"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_league: Mapped[int] = mapped_column(Integer, nullable=False)

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(15), nullable=False)
    type: Mapped[str] = mapped_column(String(7), nullable=False)
    season: Mapped[int] = mapped_column(Integer, nullable=False)
    start_league: Mapped[int] = mapped_column(Integer, nullable=False)
    end_league: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[Optional[str]] = mapped_column(String(250), nullable=False)

    metadata_league_fk: Mapped[List["LeaguesMetadata"]] = relationship(back_populates="fk_metadata_league")
    league_fixture: Mapped[List["Fixtures"]] = relationship(back_populates="fixture_league")
    league_player_stat_fk: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_league_fk")
    league_team_fixture_stat_fk: Mapped[List["TeamsFixturesStats"]] = relationship(back_populates="team_fixture_stat_league_fk")
    league_team_cards_stats_fk: Mapped[List["TeamsCardsStats"]] = relationship(back_populates="team_cards_stats_league_fk")
    league_team_goals_stats_fk: Mapped[List["TeamsGoalsStats"]] = relationship(back_populates="team_goals_stats_league_fk")

