def team_league_fixtures_stats_parser(team_league_stats_infos: dict[str:any]) -> dict[str:any]:
    idLeagueEx = team_league_stats_infos.get("league").get("id")
    idTeam = team_league_stats_infos.get("team").get("id")
    fixturesRoot = team_league_stats_infos.get("fixtures")
    cleanSheetRoot = team_league_stats_infos.get("clean_sheet")
    failedToScoreRoot = team_league_stats_infos.get("failed_to_score")
    streakRoot = team_league_stats_infos.get("biggest")

    fixturesHome = fixturesRoot.get("played").get("home")
    fixturesAway = fixturesRoot.get("played").get("away")
    fixturesWinsHome = fixturesRoot.get("wins").get("home")
    fixturesWinsAway = fixturesRoot.get("wins").get("away")
    fixturesDrawsHome = fixturesRoot.get("draws").get("home")
    fixturesDrawsAway = fixturesRoot.get("draws").get("away")
    fixturesLosesHome = fixturesRoot.get("loses").get("home")
    fixturesLosesAway = fixturesRoot.get("loses").get("away")

    cleanSheetsHome = cleanSheetRoot.get("home")
    cleanSheetsAway = cleanSheetRoot.get("away")

    failedToScoreHome = failedToScoreRoot.get("home")
    failedToScoreAway = failedToScoreRoot.get("away")

    maxWinStreak = streakRoot.get("streak").get("wins")
    maxDrawStreak = streakRoot.get("streak").get("draws")
    maxLoseStreak = streakRoot.get("streak").get("loses")

    betterWinHome = streakRoot.get("wins").get("home")
    betterWinAway = streakRoot.get("wins").get("away")
    worstLoseHome = streakRoot.get("loses").get("home")
    worstLoseAway = streakRoot.get("loses").get("away")

    dictToReturn = {
        "id_team": idTeam, "id_league": idLeagueEx, "fixtures_home": fixturesHome, "fixtures_away": fixturesAway,
        "wins_home": fixturesWinsHome, "wins_away": fixturesWinsAway, "draws_home": fixturesDrawsHome,
        "draws_away": fixturesDrawsAway, "loses_home": fixturesLosesHome, "loses_away": fixturesLosesAway,
        "clean_sheets_home": cleanSheetsHome, "clean_sheets_away": cleanSheetsAway,
        "not_scored_home": failedToScoreHome,
        "not_scored_away": failedToScoreAway, "max_wins_streak": maxWinStreak, "max_draws_streak": maxDrawStreak,
        "max_loses_streak": maxLoseStreak, "better_win_home": betterWinHome, "better_win_away": betterWinAway,
        "worst_lose_home": worstLoseHome, "worst_lose_away": worstLoseAway
    }

    for keyValue in list(dictToReturn.keys()):
        valueDict = dictToReturn.get(keyValue)
        if valueDict is None:
            dictToReturn.update({keyValue: 0})

    return dictToReturn


def team_league_cards_stats_parser(team_league_cards_stats_infos: dict[str:any]) -> dict[str:str]:
    cardTypes = ["red", "yellow"]

    idLeagueEx = team_league_cards_stats_infos.get("league").get("id")
    idTeam = team_league_cards_stats_infos.get("team").get("id")
    cardsRoot = team_league_cards_stats_infos.get("cards")
    listToReturn: list[dict[str:any]] = []

    for cardType in cardTypes:
        cardTypeRoot = cardsRoot.get(cardType)
        minute0_15 = cardTypeRoot.get("0-15").get("total")
        minute16_30 = cardTypeRoot.get("16-30").get("total")
        minute31_45 = cardTypeRoot.get("31-45").get("total")
        minute46_60 = cardTypeRoot.get("46-60").get("total")
        minute61_75 = cardTypeRoot.get("61-75").get("total")
        minute76_90 = cardTypeRoot.get("76-90").get("total")
        minute91_105 = cardTypeRoot.get("91-105").get("total")
        minute106_120 = cardTypeRoot.get("106-120").get("total")

        dictToReturn = {
            "id_league": idLeagueEx, "id_team": idTeam, "card_type": cardType, "in_minute_0_15": minute0_15,
            "in_minute_16_30": minute16_30, "in_minute_31_45": minute31_45, "in_minute_46_60": minute46_60,
            "in_minute_61_75": minute61_75, "in_minute_76_90": minute76_90, "in_minute_91_105": minute91_105,
            "in_minute_106_120": minute106_120
        }

        for keyValue in list(dictToReturn.keys()):
            valueStat = dictToReturn.get(keyValue)
            if valueStat is None:
                dictToReturn.update({keyValue: 0})

        listToReturn.append(dictToReturn)

    return listToReturn