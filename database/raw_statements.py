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

def games_round(round:int, id_league:int, season:int):
    return f"""
    select fx.id from ftd.fixtures fx 
    inner join ftd.leagues l on l.id = fx.id_league 
    where status != 'match_finished'
    and l.id_league = {id_league}
    and l.season = {season}
    and cast(replace("round",'Regular Season -', '') as integer) = {round}
    """