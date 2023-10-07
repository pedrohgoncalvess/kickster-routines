from api_sports.api_requests import APIRequest
from database.raw_statements import games_played_round
from routines.fixtures.parser import fixture_parser
from routines.fixtures.metadata import check_rounds_brasileirao, insert_metadata
from configs import actual_season


def att_rounds_brasileirao():
    from database.connection import DatabaseConnection

    dbConnection = DatabaseConnection()

    leagueMetadata = dbConnection.leagues_metadata(71)[0]

    idLeague = leagueMetadata.get("id_league")
    seasonLeague = actual_season()
    gamesRoundLeague = leagueMetadata.get("games_round")
    idMetadata = leagueMetadata.get("id_metadata")

    roundsPlayed = dbConnection.execute(games_played_round(idLeague, seasonLeague))

    idLeagueMtd = 2 #metadata brasileirao
    roundsIncomplet = dbConnection.incomplet_rounds_metadata(idLeagueMtd)
    roundsPlayed = dbConnection.leagues_metadata()



def main():

    roundsChecked = check_rounds_brasileirao()

    insert_metadata(roundsChecked)

def collect_fixture(id_fixture: int):

    requestClass = APIRequest()
    fixtureBasicsInfos = requestClass.fixture_basics(id_fixture)
    treatedInfos = fixture_parser(fixtureBasicsInfos[0])
    return treatedInfos


def update_fixture(fixture_infos):
    from sqlalchemy import select
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


#update_fixture(collect_fixture(1005893))
main()
