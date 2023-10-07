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

def fixtures_to_collect_round(round:int, id_league:int, season:int):
    return f"""
    select fx.id from ftd.fixtures fx 
    inner join ftd.leagues l on l.id = fx.id_league 
    where status != 'match_finished'
    and l.id_league = {id_league}
    and l.season = {season}
    and cast(replace("round",'Regular Season -', '') as integer) = {round}
    """

def incompleted_rounds_metadata(id_league_mtd:int):
    return f"""select mr.* from mtd.rounds mr inner join mtd.leagues ml on ml.id = mr.id_league_mtd where mr.played != (select games_round from mtd.leagues where id = {id_league_mtd}) and mr.id_league_mtd = {id_league_mtd}"""

def leagues_metadata(id_league:int):
    return f"""select fl.id_league,ml.* from mtd.leagues ml inner join ftd.leagues fl on fl.id = ml.id_league where ml.status = true and fl.id_league = {id_league}"""