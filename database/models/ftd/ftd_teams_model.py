from sqlalchemy import Boolean, Integer, String, ForeignKey, types, func, Numeric
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from database.models.declarative_base import Base


class Teams(Base):
    __tablename__ = "teams"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_stadium: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.stadiums.id"), nullable=True)

    code: Mapped[Optional[str]] = mapped_column(String(3), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(15), nullable=False)
    logo: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    founded: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    national: Mapped[bool] = mapped_column(Boolean, nullable=False)

    home_stadium: Mapped["Stadiums"] = relationship(back_populates="stadium_team")
    fixture_team_home = relationship("Fixtures", back_populates="team_home", foreign_keys="[Fixtures.id_team_home]")
    fixture_team_away = relationship("Fixtures", back_populates="team_away", foreign_keys="[Fixtures.id_team_away]")
    team_fixture_stat_fk: Mapped[List["FixturesStats"]] = relationship(back_populates="fixture_stat_team_fk")
    team_player_stat_fk: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_team_fk")

    fk_team_squad: Mapped[List["TeamsSquad"]] = relationship(back_populates="team_squad_fk")
    fk_team_fixture_event: Mapped[List["FixturesEvents"]] = relationship(back_populates="fixture_event_team_fk")
    fk_team_fixture_stat: Mapped[List["TeamsFixturesStats"]] = relationship(back_populates="team_fixture_stat_fk")
    fk_team_cards_stat: Mapped[List["TeamsCardsStats"]] = relationship(back_populates="team_cards_stat_fk")
    fk_team_goals_stat: Mapped[List["TeamsGoalsStats"]] = relationship(back_populates="team_goals_stat_fk")
    fk_fixture_lineup_team: Mapped[List["FixturesLineups"]] = relationship(back_populates="fixture_lineup_team_fk")

class TeamsSquad(Base):
    __tablename__ = "teams_squad"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_player: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False, unique=True)

    shirt_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    position: Mapped[str] = mapped_column(String(30), nullable=True)
    injured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_squad_fk: Mapped["Teams"] = relationship(back_populates="fk_team_squad")
    team_squad_player_fk: Mapped["Players"] = relationship(back_populates="fk_player_team_squad")

class TeamsGoalsStats(Base):
    __tablename__ = "teams_goals_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)

    type: Mapped[str] = mapped_column(String(6), nullable=False)
    goals_home: Mapped[int] = mapped_column(Integer, nullable=False)
    goals_away: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_0_15: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_16_30: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_31_45: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_46_60: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_61_75: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_76_90: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_91_105: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_106_120: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_goals_stats_league_fk: Mapped["Leagues"] = relationship(back_populates="league_team_goals_stats_fk")
    team_goals_stat_fk: Mapped["Teams"] = relationship(back_populates="fk_team_goals_stat")

class TeamsFixturesStats(Base):
    __tablename__ = "teams_fixtures_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)

    fixtures_home: Mapped[int] = mapped_column(Integer, nullable=False)
    fixtures_away: Mapped[int] = mapped_column(Integer, nullable=False)
    wins_home: Mapped[int] = mapped_column(Integer, nullable=False)
    wins_away: Mapped[int] = mapped_column(Integer, nullable=False)
    draws_home: Mapped[int] = mapped_column(Integer, nullable=False)
    draws_away: Mapped[float] = mapped_column(Numeric, nullable=False)
    loses_home: Mapped[int] = mapped_column(Integer, nullable=False)
    loses_away: Mapped[int] = mapped_column(Integer, nullable=False)
    clean_sheets_home: Mapped[int] = mapped_column(Integer, nullable=False)
    clean_sheets_away: Mapped[int] = mapped_column(Integer, nullable=False)
    not_scored_home: Mapped[int] = mapped_column(Integer, nullable=False)
    not_scored_away: Mapped[int] = mapped_column(Integer, nullable=False)
    max_wins_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    max_draws_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    max_loses_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    better_win_home: Mapped[int] = mapped_column(Integer, nullable=False)
    worst_lose_home: Mapped[int] = mapped_column(Integer, nullable=False)
    better_win_away: Mapped[int] = mapped_column(Integer, nullable=False)
    worst_lose_away: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_fixture_stat_league_fk: Mapped["Leagues"] = relationship(back_populates="league_team_fixture_stat_fk")
    team_fixture_stat_fk: Mapped["Teams"] = relationship(back_populates="fk_team_fixture_stat")

class TeamsCardsStats(Base):
    __tablename__ = "teams_cards_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)

    card_type: Mapped[str] = mapped_column(String(6), nullable=False)
    in_minute_0_15: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_16_30: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_31_45: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_46_60: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_61_75: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_76_90: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_91_105: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_106_120: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_cards_stats_league_fk: Mapped["Leagues"] = relationship(back_populates="league_team_cards_stats_fk")
    team_cards_stat_fk: Mapped["Teams"] = relationship(back_populates="fk_team_cards_stat")