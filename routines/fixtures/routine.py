from api_sports.api_requests import APIRequest
from routines.fixtures.parser import fixture_parser
from sqlalchemy import select
from configs import actual_season


def fixtures_to_collect(id_league: int = 71):
    from database.connection import DatabaseConnection

    dbConnection = DatabaseConnection()
    leaguesMetadata = dbConnection.leagues_metadata(id_league)
    idMetadata = leaguesMetadata.get("id_metadata")
    idLeague = leaguesMetadata.get("id_league")
    seasonLeague = actual_season()

    fixturesId = []
    roundsInDatabase = dbConnection.incomplet_rounds_metadata(idMetadata)
    incompletRounds = roundsInDatabase.get("rounds")
    for roundToCollect in incompletRounds:
        _round = roundToCollect.get("round")
        fixturesToCollectOfRound = dbConnection.fixtures_to_collect(_round,idLeague,seasonLeague)
        for fixtureIdOnRound in fixturesToCollectOfRound:
            fixturesId.append(fixtureIdOnRound)

    return fixturesId


def collect_fixture(id_fixture: int):
    requestClass = APIRequest()
    fixtureBasicsInfos = requestClass.fixture_basics(id_fixture)
    treatedInfos = fixture_parser(fixtureBasicsInfos[0])
    return treatedInfos


def update_fixture(fixture_infos):
    from database.models.ftd.ftd_fixtures_model import Fixtures
    from database.connection import DatabaseConnection

    dbConnection = DatabaseConnection()
    session = dbConnection.local_session()

    idFixture = fixture_infos.get("id_fixture")
    fixtureDb = session.execute(select(Fixtures).filter_by(id=idFixture)).scalar_one()
    fixtureDb.result = fixture_infos.get("result")
    fixtureDb.referee = fixture_infos.get("referee")
    fixtureDb.status = fixture_infos.get("status")
    fixtureDb.goals_home = fixture_infos.get("goals_home")
    fixtureDb.goals_away = fixture_infos.get("goals_away")
    fixtureDb.start_at = fixture_infos.get("date")
    session.commit()
    session.close()
