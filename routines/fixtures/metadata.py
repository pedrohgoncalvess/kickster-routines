from database.connection import DatabaseConnection
from database.raw_statements import games_played_round, games_round
from configs import metadata_reader


def check_rounds_brasileirao():
    dbConnection = DatabaseConnection()
    leaguesMetadata = metadata_reader()

    idLeague = leaguesMetadata.get("id_league")
    seasonLeague = leaguesMetadata.get("season")
    gamesRoundLeague = leaguesMetadata.get("games_round")

    roundsPlayed = dbConnection.execute(games_played_round(idLeague, seasonLeague))

    dictWithRounds = {"id_league": idLeague, "season": seasonLeague}
    listWithRounds = []
    lastRoundPlayed = roundsPlayed[-1][0]
    gamesPlayedInLastRound = roundsPlayed[-1][1]
    for roundLeague in roundsPlayed:
        gamesPlayedInRound = roundLeague[1]
        actualRoundLeague = roundLeague[0]
        listWithRounds.append({actualRoundLeague: gamesPlayedInRound})
    if gamesPlayedInLastRound > (gamesRoundLeague * 0.7):
        listWithRounds.append({lastRoundPlayed + 1: 0})
    dictWithRounds.update({"rounds": listWithRounds})
    return dictWithRounds


def fixtures_to_collect(round_games: dict[str:any]):
    dbConnection = DatabaseConnection()
    leaguesMetadata = metadata_reader()

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
