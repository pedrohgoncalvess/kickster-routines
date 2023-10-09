from sqlalchemy import select
from database.connection import DatabaseConnection
from database.operations import dbOperations
from configs import actual_season


def att_metadata_rounds_brasileirao():
    dbConnection = DatabaseConnection()
    leagueMetadata = dbConnection.leagues_metadata(71)

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
        listWithRounds.append({"round":roundNumber, "games_played":gamesPlayedInRound})
    if gamesPlayedInLastRound > (gamesRoundLeague * 0.7):
        listWithRounds.append({"round": lastRoundPlayed+1, "games_played":0})
    dictWithRounds.update({"rounds": listWithRounds})
    return dictWithRounds


def insert_metadata(rounds_games:dict[str:any]):
    from database.models.mtd.mtd_rounds_model import RoundsMetadata

    for roundNumber, roundGame in enumerate(rounds_games.get("rounds"), start=1):
        newRoundMetadata = RoundsMetadata(
            id_league_mtd=rounds_games.get("id_metadata"),
            round=roundGame.get("round"),
            played=roundGame.get("games_played")
        )
        dbOperations.save_object(newRoundMetadata)


def att_rounds_brasileirao():
    from database.connection import DatabaseConnection
    from database.models.mtd.mtd_rounds_model import RoundsMetadata

    dbConnection = DatabaseConnection()
    leagueMetadata = dbConnection.leagues_metadata(71)

    idLeague = leagueMetadata.get("id_league")
    seasonLeague = actual_season()
    idMetadata = leagueMetadata.get("id_metadata")

    roundsIncomplet = dbConnection.incomplet_rounds_metadata(idMetadata)
    roundsPlayed = dbConnection.fixtures_played_round(idLeague, seasonLeague)

    for roundIncomplet in roundsIncomplet.get("rounds"):
        actualRound = roundIncomplet.get("round")
        gamesPlayed = roundIncomplet.get("games_played")
        for roundInDb in roundsPlayed:
            actualRoundInDb = roundInDb.get("round")
            if (actualRound == actualRoundInDb):
                gamesPlayedInActualRoundInDb = roundInDb.get("games_played")
                if (gamesPlayedInActualRoundInDb != gamesPlayed):
                    session = dbConnection.local_session()
                    attRoundMetadata = session.execute(select(RoundsMetadata).filter_by(id_league_mtd=idMetadata, round=actualRoundInDb)).scalar_one()
                    attRoundMetadata.played = gamesPlayedInActualRoundInDb
                    session.commit()
                    session.close()
