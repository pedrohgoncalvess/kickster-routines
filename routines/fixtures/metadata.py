from database.connection import DatabaseConnection
from database.raw_statements import games_played_round, games_round
from configs import actual_season


def check_rounds_brasileirao():
    dbConnection = DatabaseConnection()
    leagueMetadata = dbConnection.leagues_metadata(71)[0]

    idLeague = leagueMetadata.get("id_league")
    seasonLeague = actual_season()
    gamesRoundLeague = leagueMetadata.get("games_round")
    idMetadata = leagueMetadata.get("id_metadata")

    roundsPlayed = dbConnection.fixtures_played_round(idLeague, seasonLeague)

    dictWithRounds = {"id_league": idLeague, "season": seasonLeague, "id_metadata":idMetadata, "games_per_round":gamesRoundLeague}
    listWithRounds = []
    lastRoundPlayed = roundsPlayed[-1].get('round')
    gamesPlayedInLastRound = roundsPlayed[-1].get('games_played')
    for roundNumber, roundLeague in enumerate(roundsPlayed, start=1):
        gamesPlayedInRound = roundLeague.get("games_played")
        listWithRounds.append({"rounds":roundNumber, "games_played":gamesPlayedInRound})
    if gamesPlayedInLastRound > (gamesRoundLeague * 0.7):
        listWithRounds.append({lastRoundPlayed + 1: 0})
    dictWithRounds.update({"rounds": listWithRounds})
    return dictWithRounds


def insert_metadata(rounds_games:dict[str:any]):
    from database.models.mtd.mtd_rounds_model import RoundsMetadata
    from database.connection import DatabaseConnection

    dbConnection = DatabaseConnection()

    gamesPerRound = rounds_games.get("games_per_round")
    for roundNumber, roundGame in enumerate(rounds_games.get("rounds"), start=1):
        newRoundMetadata = RoundsMetadata(
            id_league_mtd=rounds_games.get("id_metadata"),
            round=roundNumber,
            status= 'completed' if roundGame.get(roundNumber) == gamesPerRound else 'incomplet'
        )
        dbConnection.execute_orm(newRoundMetadata)


def fixtures_to_collect():
    dbConnection = DatabaseConnection()
    leaguesMetadata = dbConnection.leagues_metadata()
    round_games = {}

    idLeague = leaguesMetadata.get("id_league")
    seasonLeague = leaguesMetadata.get("season")
    gamesRound = leaguesMetadata.get("games_round")

    rounds: list[dict[int:int]] = round_games.get("rounds")
    fixturesId = []
    for idx, roundPlayed in enumerate(rounds):
        roundNumber = idx + 1
        if roundPlayed.get(roundNumber) != gamesRound:
            roundsInQuery = dbConnection.execute(games_round(roundNumber, idLeague, seasonLeague))
            for roundToCollect in roundsInQuery:
                fixturesId.append(roundToCollect[0])

    return fixturesId
