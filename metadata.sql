create schema if not exists mtd;

CREATE OR REPLACE FUNCTION updated_at_with_current_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = current_timestamp;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_metadata(id_metadata integer, "round" integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_metadata || '-' || "round";
END;
$$ LANGUAGE plpgsql;

create table if not exists mtd.leagues (
    id serial,
    id_league integer unique not null,
    total_rounds integer not null,
    games_round integer not null,
    status bool not null,
    created_at timestamp default current_timestamp,

    constraint metadata_league_pk primary key (id),
    constraint metadata_league_fk foreign key (id_league) references "ftd".leagues (id)
);

create table if not exists mtd.rounds (
	id serial,
	id_league_mtd integer not null,
	"round" integer not null,
	played integer not null,
	updated_at timestamp default current_timestamp,
	id_compost varchar(20) unique generated always as (generate_compost_id_metadata(id_league_mtd, "round")) stored,

	constraint metadata_pk primary key (id),
	constraint metadata_fixture_fk foreign key (id_league_mtd) references "mtd".leagues (id)
);

CREATE TRIGGER trigger_att_updated_at_mtd_rounds
BEFORE INSERT OR UPDATE ON mtd.rounds
FOR EACH ROW
EXECUTE FUNCTION updated_at_with_current_timestamp();

create table if not exists mtd.fixtures (
    id serial,
    id_fixture integer not null unique,
    stats_metadata varchar(13) not null,
    lineups_metadata varchar(13) not null,
    events_metadata varchar(13) not null,
    updated_at timestamp default current_timestamp,

    constraint metadata_fixture_pk primary key (id),
    constraint metadata_fixture_fk foreign key (id_fixture) references "ftd".fixtures (id)
);

CREATE TRIGGER trigger_att_updated_at_mtd_fixtures
BEFORE INSERT OR UPDATE ON mtd.fixtures
FOR EACH ROW
EXECUTE FUNCTION updated_at_with_current_timestamp();

create table if not exists mtd.teams (
    id serial,
    id_team integer not null unique,
    team_squad timestamp default current_timestamp not null,
    teams_cards timestamp default current_timestamp not null,
    teams_goals timestamp default current_timestamp not null,
    teams_fixtures timestamp default current_timestamp not null,

    constraint metadata_teams_pk primary key (id)
);