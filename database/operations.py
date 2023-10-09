from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from database.connection import DatabaseConnection
from database.models.mtd.mtd_fixtures_model import FixturesMetadata


class DatabaseOperations(DatabaseConnection):
    def upsert_fixtures_infos(self, fixture_metadata: FixturesMetadata):
        session = self.local_session()
        try:
            session.add(fixture_metadata)
            session.commit()
        except IntegrityError:
            session.rollback()
            fixtureInfoToUpdate = session.execute(select(FixturesMetadata).filter_by(id_fixture=fixture_metadata.id_fixture)).scalar_one()
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


dbOperations = DatabaseOperations()
