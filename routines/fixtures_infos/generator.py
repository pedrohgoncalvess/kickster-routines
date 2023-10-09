from database.models.ftd.ftd_fixtures_model import FixturesStats, FixturesEvents, FixturesLineups


def generator_fixture_stats(team_fixture_stats_infos: dict[str:any]) -> FixturesStats:
    idFixture = team_fixture_stats_infos.get("id_fixture")
    idTeam = team_fixture_stats_infos.get("id_team")
    formation = team_fixture_stats_infos.get("formation")
    idCoach = team_fixture_stats_infos.get("coach")
    shotsOnGoal = team_fixture_stats_infos.get("shots_on_goal")
    shotsOffGoal = team_fixture_stats_infos.get("shots_off_goal")
    shotsBlocked = team_fixture_stats_infos.get("blocked_shots")
    shotsInsideBox = team_fixture_stats_infos.get("shots_insidebox")
    shotsOffsideBox = team_fixture_stats_infos.get("shots_outsidebox")
    fouls = team_fixture_stats_infos.get("fouls")
    cornerKicks = team_fixture_stats_infos.get("corner_kicks")
    offSides = team_fixture_stats_infos.get("offsides")
    ballPossession = team_fixture_stats_infos.get("ball_possession")
    yellowCards = team_fixture_stats_infos.get("yellow_cards")
    redCards = team_fixture_stats_infos.get("red_cards")
    goalKeeperSaves = team_fixture_stats_infos.get("goalkeeper_saves")
    totalPasses = team_fixture_stats_infos.get("total_passes")
    accuratePasses = team_fixture_stats_infos.get("passes_accurate")
    expectedGoals = team_fixture_stats_infos.get("expected_goals")

    newFixtureStat = FixturesStats(
        id_fixture=idFixture, id_team=idTeam, id_coach=idCoach, formation=formation, shots_on_goal=shotsOnGoal,
        shots_off_goal=shotsOffGoal, shots_blocked=shotsBlocked, shots_inside_box=shotsInsideBox,
        shots_offside_box=shotsOffsideBox,
        fouls=fouls, corners=cornerKicks, offsides=offSides, possession=ballPossession, yellow_cards=yellowCards,
        red_cards=redCards,
        goalkeeper_saves=goalKeeperSaves, total_passes=totalPasses, accurate_passes=accuratePasses,
        expected_goals=expectedGoals
    )

    return newFixtureStat


def generator_fixture_event(fixture_events_infos: dict[str:any]) -> FixturesEvents:
    idTeam = fixture_events_infos.get("id_team")
    idFixture = fixture_events_infos.get("id_fixture")
    timeElapsed = fixture_events_infos.get("time")
    idPrincipalPlayer = fixture_events_infos.get("id_player_principal")
    idPlayerAssist = fixture_events_infos.get("id_player_assist")
    typeEvent = fixture_events_infos.get("type")
    detailEvent = fixture_events_infos.get("detail")
    commentEvent = fixture_events_infos.get("comment")

    newFixtureEvents = FixturesEvents(
        id_team=idTeam, id_fixture=idFixture, time=timeElapsed, id_player_principal=idPrincipalPlayer,
        id_player_assist=idPlayerAssist, type_event=typeEvent, detail=detailEvent, comments=commentEvent
    )

    return newFixtureEvents


def generator_fixture_lineup(fixture_lineup_infos: dict[str:any]) -> FixturesLineups:
    idTeam = fixture_lineup_infos.get("id_team")
    idFixture = fixture_lineup_infos.get("id_fixture")
    idPlayer = fixture_lineup_infos.get("id_player")
    typeLineUp = fixture_lineup_infos.get("type")
    positionPlayer = fixture_lineup_infos.get("position")
    gridPlayer = fixture_lineup_infos.get("grid")

    newFixtureLineup = FixturesLineups(
        id_team=idTeam, id_fixture=idFixture, id_player=idPlayer,
        type=typeLineUp, position=positionPlayer, grid=gridPlayer
    )

    return newFixtureLineup
