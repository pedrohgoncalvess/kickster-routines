from database.operations import dbOperations
from routines.fixtures.fixtures_infos.routine import add_fixture_stat, add_fixture_events, add_fixture_lineups


def main():
    from database.raw_statements import query_fixtures_infos_metadata
    from routines.fixtures.fixtures_infos.routine import fixtures_metadata_att

    fixtures_metadata_att()

    query = query_fixtures_infos_metadata(71)
    results = dbOperations.execute_stmt(query)
    for result in results:
        idFixture = result[0]
        statsMetadata = result[1]
        eventsMetadata = result[2]
        lineupsMetadata = result[3]

        if statsMetadata == 'not_collected':
            add_fixture_stat(idFixture)
        if eventsMetadata == 'not_collected':
            add_fixture_events(idFixture)
        if lineupsMetadata == 'not_collected':
            add_fixture_lineups(idFixture)

    fixtures_metadata_att()

if __name__ == '__main__':
    main()