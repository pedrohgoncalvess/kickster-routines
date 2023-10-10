def intern_id_league(id_league: int, season: int):
    return f"select id from ftd.leagues where id_league = {id_league} and season = {season}"


def games_played_round(id_league: int, season: int):
    return f"""
    select cast(replace("round",'Regular Season -', '') as integer) "round", count("round") from ftd.fixtures fx
    inner join ftd.leagues l on l.id = fx.id_league
    where status = 'match_finished'
    and l.id_league = {id_league}
    and l.season = {season}
    group by cast(replace("round",'Regular Season -', '') as integer)
    order by cast(replace("round",'Regular Season -', '') as integer)
    """


def fixtures_to_collect_round(round: int, id_league: int, season: int):
    return f"""
    select fx.id from ftd.fixtures fx 
    inner join ftd.leagues l on l.id = fx.id_league 
    where status != 'match_finished'
    and l.id_league = {id_league}
    and l.season = {season}
    and cast(replace("round",'Regular Season -', '') as integer) = {round}
    """


def incompleted_rounds_metadata(id_league_mtd: int):
    return f"""select mr.* from mtd.rounds mr inner join mtd.leagues ml on ml.id = mr.id_league_mtd where mr.played != (select games_round from mtd.leagues where id = {id_league_mtd}) and mr.id_league_mtd = {id_league_mtd}"""


def leagues_metadata(id_league: int):
    return f"""select fl.id_league,ml.* from mtd.leagues ml inner join ftd.leagues fl on fl.id = ml.id_league where ml.status = true and fl.id_league = {id_league}"""


def fixtures_infos_metadata(id_league: int):
    return f"""
    select distinct(fx.id) id_fixture,  fs.id_fixture stats, fl.id_fixture lineups, fe.id_fixture events from ftd.fixtures fx
    left join ftd.fixtures_stats fs on fs.id_fixture = fx.id
    left join ftd.fixtures_events fe on fe.id_fixture = fx.id
    left join ftd.fixtures_lineups fl on fl.id_fixture = fx.id
    where fx.status = 'match_finished'
    and id_league = (select fl.id from ftd.leagues fl where fl.id_league = {id_league})
    """


def query_fixtures_infos_metadata(id_league: int):
    return f"""
    select id_fixture, stats_metadata, events_metadata, lineups_metadata from mtd.fixtures mfx
    inner join ftd.fixtures ffx on ffx.id = mfx.id_fixture
    inner join ftd.leagues l on l.id = ffx.id_league
    where l.id_league = {id_league}
    and stats_metadata != 'collected'
    or events_metadata != 'collected'
    or lineups_metadata != 'collected'
    """


def query_fixtures_infos_all_collected(id_league: int):
    return f"""
    select id_fixture from mtd.fixtures mfx
    inner join ftd.fixtures ffx on ffx.id = mfx.id_fixture
    inner join ftd.leagues l on l.id = ffx.id_league
    where l.id_league = {id_league}
    and lineups_metadata = 'collected'
    and stats_metadata = 'collected'
    and events_metadata = 'collected'
    """


def query_teams_fixtures_stats_to_collect(id_league: int):
    return f"""
    select id_team, l.id_league from ftd.teams_fixtures_stats tfs
    inner join ftd.leagues l on l.id = tfs.id_league
    where date(updated_at) < current_date -5
    and l.id_league = {id_league}
    """


def query_teams_cards_stats_to_collect(id_league: int):
    return f"""
    select id_team, l.id_league from ftd.teams_cards_stats tcs
    inner join ftd.leagues l on l.id = tcs.id_league
    where date(updated_at) < current_date -5
    and l.id_league = {id_league}
    """
