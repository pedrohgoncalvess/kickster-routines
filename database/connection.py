from configs import get_var
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class DatabaseConnection:
    def __init__(self):
        self.host = get_var('DB_HOST')
        self.port = get_var('DB_PORT')
        self.dbName = get_var('DB_NAME')
        self.user = get_var('DB_USER')
        self.password = get_var('DB_PASSWORD')
        self.__engine__ = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbName}"
        )


    def execute(self, raw_statement: str):
        with self.__engine__.connect() as connection:
            statement = text(raw_statement)
            cursorStatement = connection.execute(statement)
            resultOfQuery = cursorStatement.fetchall()
        return resultOfQuery

    def local_session(self):
        return Session(self.__engine__)

    def execute_orm(self, objectToSave):
        session = self.local_session()
        try:
            session.add(objectToSave)
            session.commit()
        except Exception as error:
            print(error)
        finally:
            session.close()


    def leagues_metadata(self, id_league: int = 71):
        from database.raw_statements import leagues_metadata

        query = leagues_metadata(id_league)
        results = self.execute(query)
        listOfLeaguesMetadata = []
        for result in results:
            listOfLeaguesMetadata.append(
                {"id_league":result[0],"id_metadata":result[1],"total_rounds":result[3],"games_round":result[4]}
            )
        return listOfLeaguesMetadata[0]

    def incomplet_rounds_metadata(self, id_league_metadata: int):
        from database.raw_statements import incompleted_rounds_metadata

        query = incompleted_rounds_metadata(id_league_metadata)
        results = self.execute(query)
        dictRoundIncompleted = {"id_league_mtd":id_league_metadata}
        listOfRoundsIncompleted = []
        for result in results:
            listOfRoundsIncompleted.append(
                {"round":result[2],"games_played":result[3]}
            )
        dictRoundIncompleted.update({"rounds":listOfRoundsIncompleted})
        return dictRoundIncompleted

    def fixtures_played_round(self, id_league:int, season:int):
        from database.raw_statements import games_played_round

        query = games_played_round(id_league, season)
        results = self.execute(query)

        listOfRounds = []
        for result in results:
            listOfRounds.append(
                {"round":result[0], "games_played":result[1]}
            )
        return listOfRounds

    def fixtures_to_collect(self, _round:int, id_league:int, season:int):
        from database.raw_statements import fixtures_to_collect_round

        query = fixtures_to_collect_round(_round, id_league, season)
        results = self.execute(query)

        listOfFixtures = []
        for result in results:
            listOfFixtures.append(result[0])
        return listOfFixtures
