def games_played_round():
    return """
    select cast(replace("round",'Regular Season -', '') as integer) "round", count("round") from ftd.fixtures
    where status = 'match_finished'
    group by cast(replace("round",'Regular Season -', '') as integer)
    order by cast(replace("round",'Regular Season -', '') as integer)
    """