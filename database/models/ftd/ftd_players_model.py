from sqlalchemy import Numeric, Boolean, Integer, String, ForeignKey, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from database.models.declarative_base import Base
from sqlalchemy import types


class Players(Base):
    __tablename__ = "players"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    date_of_birth: Mapped[Optional[types.Date]] = mapped_column(String(20), nullable=True)

    nationality: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    weight: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    image: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)

    fk_player_stat: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_fk")
    fk_player_team_squad: Mapped[List["TeamsSquad"]] = relationship(back_populates="team_squad_player_fk")
    fk_fixture_event_principal_player = relationship("FixturesEvents", back_populates="fixture_event_principal_player_fk", foreign_keys="[FixturesEvents.id_player_principal]")
    fk_fixture_event_assist_player = relationship("FixturesEvents", back_populates="fixture_event_assist_player_fk", foreign_keys="[FixturesEvents.id_player_assist]")
    fk_fixture_lineup_player: Mapped[List["FixturesLineups"]] = relationship(back_populates="fixture_lineup_player_fk")

class PlayersStats(Base):
    __tablename__ = "players_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_player: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)
    id_team: Mapped[str] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)

    position: Mapped[str] = mapped_column(String(30), nullable=False)
    captain: Mapped[bool] = mapped_column(Boolean, nullable=False)
    appearances: Mapped[int] = mapped_column(Integer, nullable=False)
    lineups: Mapped[int] = mapped_column(Integer, nullable=False)
    minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Numeric, nullable=False)
    substitutes_in: Mapped[int] = mapped_column(Integer, nullable=False)
    substitutes_out: Mapped[int] = mapped_column(Integer, nullable=False)
    bench: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_total: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_on: Mapped[int] = mapped_column(Integer, nullable=False)
    goals: Mapped[int] = mapped_column(Integer, nullable=False)
    assists: Mapped[int] = mapped_column(Integer, nullable=False)
    conceded_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    saved_goals: Mapped[int] = mapped_column(Integer, nullable=False)
    total_pass: Mapped[int] = mapped_column(Integer, nullable=False)
    key_pass: Mapped[int] = mapped_column(Integer, nullable=False)
    accuracy_pass: Mapped[int] = mapped_column(Integer, nullable=False)
    tackles: Mapped[int] = mapped_column(Integer, nullable=False)
    blocks: Mapped[int] = mapped_column(Integer, nullable=False)
    interceptions: Mapped[int] = mapped_column(Integer, nullable=False)
    total_duels: Mapped[int] = mapped_column(Integer, nullable=False)
    win_duels: Mapped[int] = mapped_column(Integer, nullable=False)
    attempted_dribbles: Mapped[int] = mapped_column(Integer, nullable=False)
    success_dribbles: Mapped[int] = mapped_column(Integer, nullable=False)
    past_dribbles: Mapped[int] = mapped_column(Integer, nullable=False)
    drawn_fouls: Mapped[int] = mapped_column(Integer, nullable=False)
    committed_fouls: Mapped[int] = mapped_column(Integer, nullable=False)
    yellow_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    yellow_red_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    red_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    won_penalties: Mapped[int] = mapped_column(Integer, nullable=False)
    committed_penalties: Mapped[int] = mapped_column(Integer, nullable=False)
    scored_penalties: Mapped[int] = mapped_column(Integer, nullable=False)
    missed_penalties: Mapped[int] = mapped_column(Integer, nullable=False)
    saved_penalties: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    player_stat_fk: Mapped["Players"] = relationship(back_populates="fk_player_stat")
    player_stat_league_fk: Mapped["Leagues"] = relationship(back_populates="league_player_stat_fk")
    player_stat_team_fk: Mapped["Teams"] = relationship(back_populates="team_player_stat_fk")