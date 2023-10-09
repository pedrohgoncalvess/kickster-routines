from database.operations import dbOperations
from database.models.mtd.mtd_fixtures_model import FixturesMetadata


def fixtures_metadata_att():
    from database.raw_statements import fixtures_infos_metadata, query_fixtures_infos_all_collected
    from database.operations import dbOperations

    idLeague = 71
    query = fixtures_infos_metadata(idLeague)
    results = dbOperations.execute_stmt(query)

    queryFixturesCollectedInDb = query_fixtures_infos_all_collected(idLeague)
    fixturesCollectedInDb = dbOperations.execute_stmt(queryFixturesCollectedInDb)
    fixturesCollected = []
    for fixture in fixturesCollectedInDb:
        if fixture not in fixturesCollected:
            fixturesCollected.append(fixture)

    for result in results:
        if result[0] not in fixturesCollected:
            dbOperations.upsert_fixtures_infos(
                FixturesMetadata(
                    id_fixture=result[0],
                    stats_metadata="not_collected" if result[1] == None else "collected",
                    lineups_metadata="not_collected" if result[2] == None else "collected",
                    events_metadata="not_collected" if result[3] == None else "collected"
                )
            )


def add_fixture_stat(id_fixture: int):
    from api_sports.api_requests import APIRequest
    from routines.fixtures_infos.parser import fixture_stats_parser
    from routines.fixtures_infos.generator import generator_fixture_stats

    req = APIRequest()

    fixtureStatsResponseRaw = req.fixture_stats(id_fixture)[0]
    fixtureLineUpResponseRaw = req.fixture_lineups(id_fixture)[0]
    fixtureStatsRawInfos = fixture_stats_parser(fixtureStatsResponseRaw, fixtureLineUpResponseRaw, id_fixture)
    fixtureStat = generator_fixture_stats(fixtureStatsRawInfos)
    dbOperations.save_object(fixtureStat)


def add_fixture_events(id_fixture:int):
    from api_sports.api_requests import APIRequest
    from routines.fixtures_infos.parser import fixture_events_parser
    from routines.fixtures_infos.generator import generator_fixture_event

    req = APIRequest()
    fixtureEventRaw = req.fixture_events(id_fixture)

    eventsInserted = []
    for event in fixtureEventRaw:
        fixtureEventInfo = fixture_events_parser(event, id_fixture)
        newFixtureEvent = generator_fixture_event(fixtureEventInfo)

        compostKey = f"{id_fixture}-{newFixtureEvent.id_team}-{newFixtureEvent.time}-{newFixtureEvent.type_event}"
        if compostKey not in eventsInserted:
            dbOperations.save_object(newFixtureEvent)
            eventsInserted.append(compostKey)


def add_fixture_lineups(id_fixture:int):
    from api_sports.api_requests import APIRequest
    from routines.fixtures_infos.parser import fixture_lineup_parser
    from routines.fixtures_infos.generator import generator_fixture_lineup

    req = APIRequest()
    fixtureLineUpRaw = req.fixture_lineups(id_fixture)

    for teamLineUp in fixtureLineUpRaw:
        fixtureTeamLineUp = fixture_lineup_parser(teamLineUp, id_fixture)
        for playerInLineUp in fixtureTeamLineUp:
            newPlayerInFixtureLineup = generator_fixture_lineup(playerInLineUp)
            dbOperations.save_object(newPlayerInFixtureLineup)
