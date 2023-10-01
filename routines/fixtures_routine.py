from database.connection import DatabaseConnection
from database.raw_statements import games_played_round
from configs import metadata_reader


def check_rounds():
    dbConnection = DatabaseConnection()
    roundsPlayed = dbConnection.execute(games_played_round())

    leaguesMetadata = metadata_reader()
    idLeague = leaguesMetadata.get("id_league")
    gamesRoundLeague = leaguesMetadata.get("games_round")

    dictWithRounds = {"id_league":idLeague}
    listWithRounds = []
    lastRoundPlayed = roundsPlayed[-1][0]
    gamesPlayedInLastRound = roundsPlayed[-1][1]
    for roundLeague in roundsPlayed:
        gamesPlayedInRound = roundLeague[1]
        actualRoundLeague = roundLeague[0]
        listWithRounds.append({actualRoundLeague:gamesPlayedInRound})
    if gamesPlayedInLastRound > (gamesRoundLeague*0.7):
        listWithRounds.append({lastRoundPlayed+1:0})
    dictWithRounds.update({"rounds":listWithRounds})
    return dictWithRounds


print(check_rounds())
