from routines.fixtures.metadata import check_rounds_brasileirao, insert_metadata, att_rounds_brasileirao
from routines.fixtures.routine import collect_fixture, fixtures_to_collect, update_fixture


def main():
    roundsChecked = check_rounds_brasileirao()
    insert_metadata(roundsChecked)
    att_rounds_brasileirao()
    fixturesId = fixtures_to_collect(71)
    for fixtureId in fixturesId:
        fixtureInfos = collect_fixture(fixtureId)
        update_fixture(fixtureInfos)
    att_rounds_brasileirao()
    insert_metadata(roundsChecked)


if __name__ == '__main__':
    main()