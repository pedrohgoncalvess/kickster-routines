from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from database.models.declarative_base import Base
from sqlalchemy import types
from database.models.ftd.ftd_teams_model import Teams

class Fixtures(Base):
    __tablename__ = "fixtures"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_stadium: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.stadiums.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=False)
    id_team_home: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_team_away: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)

    start_at: Mapped[types.DateTime] = mapped_column(String(20), nullable=False)
    result: Mapped[str] = mapped_column(String(11), nullable=False)
    goals_home: Mapped[int] = mapped_column(Integer, nullable=False)
    goals_away: Mapped[int] = mapped_column(Integer, nullable=False)
    round: Mapped[str] = mapped_column(String(30), nullable=False)
    referee: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    data_stats: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')
    data_events: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')
    data_lineups: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')

    team_home = relationship("Teams", back_populates="fixture_team_home", foreign_keys="[Fixtures.id_team_home]")
    team_away = relationship("Teams", back_populates="fixture_team_away", foreign_keys="[Fixtures.id_team_away]")
    fixture_league: Mapped["Leagues"] = relationship(back_populates="league_fixture")
    fixture_stadium: Mapped["Stadiums"] = relationship(back_populates="stadium_fixture")
    fixture_stat_fk: Mapped[List["FixturesStats"]] = relationship(back_populates="fixture_fk")
    fk_fixture_event: Mapped[List["FixturesEvents"]] = relationship(back_populates="fixture_event_fk")
    fk_fixture_lineup: Mapped[List["FixturesLineups"]] = relationship(back_populates="fixture_lineup_fk")
    metadata_fixture_fk: Mapped[List["FixturesMetadata"]] = relationship(back_populates="fk_metadata_fixture")


class FixturesEvents(Base):
    __tablename__ = "fixtures_events"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_player_principal: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False)
    id_player_assist: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.players.id"), nullable=True)

    time: Mapped[int] = mapped_column(Integer, nullable=False)
    type_event: Mapped[str] = mapped_column(String(20), nullable=False)
    detail: Mapped[str] = mapped_column(String(30), nullable=False)
    comments: Mapped[str] = mapped_column(String(30), nullable=False)

    fixture_event_fk: Mapped["Fixtures"] = relationship(back_populates="fk_fixture_event")
    fixture_event_team_fk: Mapped["Teams"] = relationship(back_populates="fk_team_fixture_event")
    fixture_event_principal_player_fk = relationship("Players", back_populates="fk_fixture_event_principal_player",
                                                     foreign_keys="[FixturesEvents.id_player_principal]")
    fixture_event_assist_player_fk = relationship("Players", back_populates="fk_fixture_event_assist_player",
                                                  foreign_keys="[FixturesEvents.id_player_assist]")


class FixturesLineups(Base):
    __tablename__ = "fixtures_lineups"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_player: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False)

    type: Mapped[str] = mapped_column(String(5), nullable=False)
    position: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    grid: Mapped[str] = mapped_column(String(3), nullable=False)

    fixture_lineup_fk: Mapped["Fixtures"] = relationship(back_populates="fk_fixture_lineup")
    fixture_lineup_team_fk: Mapped["Teams"] = relationship(back_populates="fk_fixture_lineup_team")
    fixture_lineup_player_fk: Mapped["Players"] = relationship(back_populates="fk_fixture_lineup_player")


class FixturesStats(Base):
    __tablename__ = "fixtures_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)

    id_coach: Mapped[int] = mapped_column(Integer, nullable=False)
    formation: Mapped[Optional[str]] = mapped_column(String(10), nullable=False)
    shots_on_goal: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_off_goal: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_blocked: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_inside_box: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_offside_box: Mapped[int] = mapped_column(Integer, nullable=False)
    fouls: Mapped[int] = mapped_column(Integer, nullable=False)
    corners: Mapped[int] = mapped_column(Integer, nullable=False)
    offsides: Mapped[int] = mapped_column(Integer, nullable=False)
    possession: Mapped[int] = mapped_column(Integer, nullable=False)
    yellow_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    red_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    goalkeeper_saves: Mapped[int] = mapped_column(Integer, nullable=False)
    total_passes: Mapped[int] = mapped_column(Integer, nullable=False)
    accurate_passes: Mapped[int] = mapped_column(Integer, nullable=False)
    expected_goals: Mapped[int] = mapped_column(Integer, nullable=False)

    fixture_fk: Mapped["Fixtures"] = relationship(back_populates="fixture_stat_fk")
    fixture_stat_team_fk: Mapped["Teams"] = relationship(back_populates="team_fixture_stat_fk")