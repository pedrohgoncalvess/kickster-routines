from database.raw_statements import query_teams_fixtures_stats_to_collect, query_teams_cards_stats_to_collect
from database.operations import dbOperations
from api_sports.api_requests import APIRequest
from configs import actual_season


def main():
    idLeague = 71

    queryTeamStats = query_teams_fixtures_stats_to_collect(idLeague)
    resultsTeamStats = dbOperations.execute_stmt(queryTeamStats)

    for resultTeamStat in resultsTeamStats:
        idTeam_stat = resultTeamStat[0]
        idLeague_stat = resultTeamStat[1]
        att_team_league_stat(idTeam_stat, idLeague_stat)

    queryTeamCards = query_teams_cards_stats_to_collect(idLeague)
    resultsTeamsCards = dbOperations.execute_stmt(queryTeamCards)
    for resultTeamCard in resultsTeamsCards:
        idTeam_card = resultTeamCard[0]
        idLeague_card = resultTeamCard[1]
        att_team_card_stat(idTeam_card, idLeague_card)


def att_team_league_stat(id_team: int, id_league: int):
    from routines.teams.data.generator import generator_team_league_fixtures_stats
    from routines.teams.data.parser import team_league_fixtures_stats_parser

    season = actual_season()

    req = APIRequest()
    idInternLeague = dbOperations.league_id_intern(id_league, season)
    teamStatsRaw = req.team_league_stats(id_team, id_league, season)
    teamStatParsed = team_league_fixtures_stats_parser(teamStatsRaw)
    newTeamStat = generator_team_league_fixtures_stats(teamStatParsed)
    newTeamStat.id_league = idInternLeague
    dbOperations.update_team_league_stats(newTeamStat)


def att_team_card_stat(id_team: int, id_league: int):
    from routines.teams.data.generator import generator_team_league_cards_stats
    from routines.teams.data.parser import team_league_cards_stats_parser

    season = actual_season()

    req = APIRequest()
    idInternLeague = dbOperations.league_id_intern(id_league, season)
    teamCardsRaw = req.team_league_stats(id_team, id_league, season)
    teamCardsParsed = team_league_cards_stats_parser(teamCardsRaw)
    for cardType in teamCardsParsed:
        newCardStat = generator_team_league_cards_stats(cardType)
        print(newCardStat.card_type)
        newCardStat.id_league = idInternLeague
        dbOperations.update_team_cards_stats(newCardStat)


main()
