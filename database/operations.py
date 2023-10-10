from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from database.connection import DatabaseConnection
from database.models.mtd.mtd_fixtures_model import FixturesMetadata
from database.models.ftd.ftd_teams_model import TeamsFixturesStats, TeamsCardsStats


class DatabaseOperations(DatabaseConnection):
    def league_id_intern(self, id_league: int, season: int):
        from database.raw_statements import intern_id_league
        query = intern_id_league(id_league, season)
        result = self.execute(query)
        return result[0][0]

    def upsert_fixtures_infos(self, fixture_metadata: FixturesMetadata):
        session = self.local_session()
        try:
            session.add(fixture_metadata)
            session.commit()
        except IntegrityError:
            session.rollback()
            fixtureInfoToUpdate = session.execute(
                select(FixturesMetadata).filter_by(id_fixture=fixture_metadata.id_fixture)).scalar_one()
            fixtureInfoToUpdate.stats_metadata = fixture_metadata.stats_metadata
            fixtureInfoToUpdate.events_metadata = fixture_metadata.events_metadata
            fixtureInfoToUpdate.lineups_metadata = fixture_metadata.lineups_metadata
            session.commit()
        finally:
            session.close()

    def execute_stmt(self, raw_statement: str):
        from sqlalchemy import text

        with self.__engine__.connect() as connection:
            statement = text(raw_statement)
            cursorStatement = connection.execute(statement)
            resultOfQuery = cursorStatement.fetchall()
        return resultOfQuery

    def save_object(self, objectToSave):
        session = self.local_session()
        try:
            session.add(objectToSave)
            session.commit()
        except Exception as error:
            print(error)
        finally:
            session.close()

    def update_team_league_stats(self, newTeamLeagueStat: TeamsFixturesStats):

        session = self.local_session()
        oldTeamLeagueStat: TeamsFixturesStats = session.execute(
            select(TeamsFixturesStats).filter_by(id_team=newTeamLeagueStat.id_team,
                                                 id_league=newTeamLeagueStat.id_league)).scalar_one()
        oldTeamLeagueStat.fixtures_away = newTeamLeagueStat.fixtures_away
        oldTeamLeagueStat.fixtures_home = newTeamLeagueStat.fixtures_home
        oldTeamLeagueStat.wins_home = newTeamLeagueStat.wins_home
        oldTeamLeagueStat.wins_away = newTeamLeagueStat.wins_away
        oldTeamLeagueStat.draws_home = newTeamLeagueStat.draws_home
        oldTeamLeagueStat.draws_away = newTeamLeagueStat.draws_away
        oldTeamLeagueStat.loses_home = newTeamLeagueStat.loses_home
        oldTeamLeagueStat.loses_away = newTeamLeagueStat.loses_away
        oldTeamLeagueStat.clean_sheets_home = newTeamLeagueStat.clean_sheets_home
        oldTeamLeagueStat.clean_sheets_away = newTeamLeagueStat.clean_sheets_away
        oldTeamLeagueStat.not_scored_home = newTeamLeagueStat.not_scored_home
        oldTeamLeagueStat.not_scored_away = newTeamLeagueStat.not_scored_away
        oldTeamLeagueStat.max_wins_streak = oldTeamLeagueStat.max_wins_streak
        oldTeamLeagueStat.max_draws_streak = oldTeamLeagueStat.max_draws_streak
        oldTeamLeagueStat.max_loses_streak = oldTeamLeagueStat.max_loses_streak
        oldTeamLeagueStat.better_win_home = newTeamLeagueStat.better_win_home
        oldTeamLeagueStat.worst_lose_home = newTeamLeagueStat.worst_lose_home
        oldTeamLeagueStat.better_win_away = newTeamLeagueStat.better_win_away
        oldTeamLeagueStat.worst_lose_away = newTeamLeagueStat.worst_lose_away
        session.commit()
        session.close()

    def update_team_cards_stats(self, newTeamCardStat: TeamsCardsStats):
        session = self.local_session()
        oldTeamCardStat: TeamsCardsStats = session.execute(
            select(TeamsCardsStats).filter_by(id_team=newTeamCardStat.id_team,
                                                 id_league=newTeamCardStat.id_league, card_type=newTeamCardStat.card_type)).scalar_one()

        oldTeamCardStat.in_minute_0_15 = newTeamCardStat.in_minute_0_15
        oldTeamCardStat.in_minute_16_30 = newTeamCardStat.in_minute_16_30
        oldTeamCardStat.in_minute_31_45 = newTeamCardStat.in_minute_46_60
        oldTeamCardStat.in_minute_61_75 = newTeamCardStat.in_minute_61_75
        oldTeamCardStat.in_minute_76_90 = newTeamCardStat.in_minute_76_90
        oldTeamCardStat.in_minute_91_105 = newTeamCardStat.in_minute_91_105
        oldTeamCardStat.in_minute_106_120 = newTeamCardStat.in_minute_106_120
        session.commit()
        session.close()


dbOperations = DatabaseOperations()
