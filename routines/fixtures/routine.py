from api_sports.api_requests import APIRequest
from routines.fixtures.parser import fixture_parser

def collect_fixture(id_fixture: int):
    requestClass = APIRequest()
    fixtureBasicsInfos = requestClass.fixture_basics(id_fixture)
    treatedInfos = fixture_parser(fixtureBasicsInfos)


def update_fixture(fixture_infos):
    from sqlalchemy import select
    from database.models.fixtures_model import Fixtures
    from database.connection import DatabaseConnection

    dbConnection = DatabaseConnection()

    idFixture = fixture_infos.get("id_fixture")
    fixtureDb = dbConnection.session.execute(select(Fixtures).filter_by(id=idFixture)).scalar_one()

