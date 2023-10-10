def fixture_stats_parser(fixture_stats_infos: dict[str:any], fixture_lineups_infos: dict[str:any], fixture_id: int):

    idTeam = fixture_stats_infos.get("team").get("id")

    global formationLineup
    global coach
    idTeamLineUp = fixture_lineups_infos.get("team").get("id")
    if idTeam == idTeamLineUp:
        formationLineup = fixture_lineups_infos.get("formation") if fixture_lineups_infos.get("formation") is not None else "0-0-0"
        coach = fixture_lineups_infos.get("coach").get("id") if fixture_lineups_infos.get("coach") is not None else 0

    statisticsRoot = fixture_stats_infos.get("statistics")
    dictToReturn: dict[str:any] = {"id_team": idTeam, "id_fixture": fixture_id,
                                   "formation": formationLineup, "coach": coach}

    for statistic in statisticsRoot:
        typeStat = statistic.get("type").lower().replace(" ", "_")
        valueStat = statistic.get("value")
        if type(valueStat) == str:
            try:
                valueStat = int(valueStat.replace("%", ""))
            except:
                valueStat = float(valueStat)
        if valueStat is None:
            valueStat = 0
        dictToReturn.update({typeStat: valueStat})

    return dictToReturn


def fixture_events_parser(fixture_event_infos: dict[str:any], fixture_id: int):
    teamEvent = fixture_event_infos.get("team").get("id")
    timeElapsed = fixture_event_infos.get("time").get("elapsed")
    principalPlayer = fixture_event_infos.get("player").get("id")
    assistPlayer = fixture_event_infos.get("assist").get("id")
    typeEvent = fixture_event_infos.get("type")
    detailEvent = fixture_event_infos.get("detail")
    commentEvent = fixture_event_infos.get("comments")

    if principalPlayer is None:
        commentEvent = "coaching_staff"

    dictToReturn = {
        "id_fixture": fixture_id,
        "id_team": teamEvent,
        "time": timeElapsed,
        "id_player_principal": principalPlayer,
        "id_player_assist": assistPlayer,
        "type": typeEvent.lower().replace(" ", "_") if type(typeEvent) == str else None,
        "detail": detailEvent.lower().replace(" ", "_") if type(detailEvent) == str else None,
        "comment": commentEvent.lower().replace(" ", "_") if type(commentEvent) == str else None
    }

    return dictToReturn


def fixture_lineup_parser(fixture_lineup_infos: dict[str:any], id_fixture: str | int) -> dict[str:any]:
    idTeam = fixture_lineup_infos.get("team").get("id")
    typesLineUps = ["startXI", "substitutes"]
    listPlayers = []

    for typeLineUp in typesLineUps:
        typeLineUpRoot = fixture_lineup_infos.get(typeLineUp)
        for player in typeLineUpRoot:
            typeLine = "start" if typeLineUp == 'startXI' else "subst"
            playerRoot = player.get("player")
            idPlayer = playerRoot.get("id")
            posPlayer = playerRoot.get("pos")
            gridPlayer = playerRoot.get("grid") if playerRoot.get("grid") is not None else "0-0"
            dictPlayer = {
                "id_fixture": id_fixture, "id_team": idTeam, "id_player": idPlayer,
                "position": posPlayer, "grid": gridPlayer, "type": typeLine
            }
            listPlayers.append(dictPlayer)

    return listPlayers
