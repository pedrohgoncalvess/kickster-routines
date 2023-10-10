from database.models.ftd.ftd_teams_model import TeamsFixturesStats, TeamsCardsStats


def generator_team_league_fixtures_stats(team_league_fixtures_stats_infos: dict[str:any]) -> TeamsFixturesStats:
    idTeam = team_league_fixtures_stats_infos.get("id_team")
    idLeague = team_league_fixtures_stats_infos.get("id_league")
    fixturesHome = team_league_fixtures_stats_infos.get("fixtures_home")
    fixturesAway = team_league_fixtures_stats_infos.get("fixtures_away")
    winsHome = team_league_fixtures_stats_infos.get("wins_home")
    winsAway = team_league_fixtures_stats_infos.get("wins_away")
    drawsHome = team_league_fixtures_stats_infos.get("draws_home")
    drawsAway = team_league_fixtures_stats_infos.get("draws_away")
    losesHome = team_league_fixtures_stats_infos.get("loses_home")
    losesAway = team_league_fixtures_stats_infos.get("loses_away")
    cleanSheetsHome = team_league_fixtures_stats_infos.get("clean_sheets_home")
    cleanSheetsAway = team_league_fixtures_stats_infos.get("clean_sheets_away")
    notScoredHome = team_league_fixtures_stats_infos.get("not_scored_home")
    notScoredAway = team_league_fixtures_stats_infos.get("not_scored_away")
    maxWinStreak = team_league_fixtures_stats_infos.get("max_wins_streak")
    maxDrawsStreak = team_league_fixtures_stats_infos.get("max_draws_streak")
    maxLosesStreak = team_league_fixtures_stats_infos.get("max_loses_streak")
    betterWinHome = team_league_fixtures_stats_infos.get("better_win_home")
    betterWinAway = team_league_fixtures_stats_infos.get("better_win_away")
    worstLoseHome = team_league_fixtures_stats_infos.get("worst_lose_home")
    worstLoseAway = team_league_fixtures_stats_infos.get("worst_lose_away")

    newTeamLeagueStat = TeamsFixturesStats(
        id_team=idTeam, id_league=idLeague, fixtures_home=fixturesHome, fixtures_away=fixturesAway, wins_home=winsHome,
        wins_away=winsAway, draws_home=drawsHome, draws_away=drawsAway, loses_home=losesHome, loses_away=losesAway,
        clean_sheets_home=cleanSheetsHome, clean_sheets_away=cleanSheetsAway, not_scored_home=notScoredHome,
        not_scored_away=notScoredAway,
        max_wins_streak=maxWinStreak, max_draws_streak=maxDrawsStreak, max_loses_streak=maxLosesStreak,
        better_win_home=betterWinHome,
        worst_lose_home=worstLoseHome, better_win_away=betterWinAway, worst_lose_away=worstLoseAway
    )

    return newTeamLeagueStat


def generator_team_league_cards_stats(team_league_cards_stats_infos: dict[str:any]) -> TeamsCardsStats:
    idTeam = team_league_cards_stats_infos.get("id_team")
    idLeague = team_league_cards_stats_infos.get("id_league")
    cardType = team_league_cards_stats_infos.get("card_type")
    inMinute0_15 = team_league_cards_stats_infos.get("in_minute_0_15")
    inMinute16_30 = team_league_cards_stats_infos.get("in_minute_16_30")
    inMinute31_45 = team_league_cards_stats_infos.get("in_minute_31_45")
    inMinute46_60 = team_league_cards_stats_infos.get("in_minute_46_60")
    inMinute61_75 = team_league_cards_stats_infos.get("in_minute_61_75")
    inMinute76_90 = team_league_cards_stats_infos.get("in_minute_76_90")
    inMinute91_105 = team_league_cards_stats_infos.get("in_minute_91_105")
    inMinute106_120 = team_league_cards_stats_infos.get("in_minute_106_120")

    newCardStatTypeCard = TeamsCardsStats(
        id_team=idTeam, id_league=idLeague, card_type=cardType, in_minute_0_15=inMinute0_15, in_minute_16_30=inMinute16_30,
        in_minute_31_45=inMinute31_45, in_minute_46_60=inMinute46_60, in_minute_61_75=inMinute61_75, in_minute_76_90=inMinute76_90,
        in_minute_91_105=inMinute91_105, in_minute_106_120=inMinute106_120
    )

    return newCardStatTypeCard
