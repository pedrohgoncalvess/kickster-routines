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
        self.session = Session(self.__engine__)

    def execute(self, raw_statement: str):
        with self.__engine__.connect() as connection:
            statement = text(raw_statement)
            cursorStatement = connection.execute(statement)
            resultOfQuery = cursorStatement.fetchall()
        return resultOfQuery