import pytz
from datetime import datetime


def fixture_parser(fixture_infos: dict[str:any]) -> dict[str:str]:
    fixtureInfos: dict[str:any] = fixture_infos.get("fixture")
    leagueInfo = fixture_infos.get("league")
    teamsInfo = fixture_infos.get("teams")
    goalsInfo = fixture_infos.get("goals")

    idFixture: str = fixtureInfos.get("id")
    refereeFixture: str = fixtureInfos.get("referee").split(",")[0] if fixtureInfos.get("referee") is not None else None

    saoPauloTimezone = pytz.timezone('America/Sao_Paulo')
    datetimeFixtureRaw = fixtureInfos.get("periods").get("first")
    datetimeFixtureProceced = saoPauloTimezone.localize(
        datetime.fromtimestamp(datetimeFixtureRaw)) if datetimeFixtureRaw is not None else datetime.utcfromtimestamp(
        946684800)
    datetimeFixture = str(datetimeFixtureProceced).replace("-03:00", "")

    idStadium: int = fixtureInfos.get("venue").get("id") if fixtureInfos.get("venue").get("id") != "null" else None
    homeTeam: str = teamsInfo.get("home").get("id")
    awayTeam: str = teamsInfo.get("away").get("id")
    roundLeague: str = leagueInfo.get("round")
    seasonLeague: int = leagueInfo.get("season")
    goalsHome = goalsInfo.get("home")
    goalsAway = goalsInfo.get("away")

    statusFixture: str = fixtureInfos.get("status").get("long").lower().replace(" ", "_")

    winnerTeamRaw: bool | str = teamsInfo.get("home").get("winner")

    if winnerTeamRaw == True:
        winnerTeam = "home_winner"
    elif winnerTeamRaw == False:
        winnerTeam = "away_winner"
    else:
        winnerTeam = "draw"

    dictToReturn = {
        "id_fixture": idFixture, "date": datetimeFixture, "referee": refereeFixture,
        "id_stadium": idStadium, "home_team": homeTeam, "away_team": awayTeam,
        "round": roundLeague, "season": seasonLeague, "result": winnerTeam,
        "status": statusFixture, "goals_home": goalsHome, "goals_away": goalsAway
    }

    return dictToReturn
