CREATE OR REPLACE FUNCTION updated_at_with_current_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = current_timestamp;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION generate_compost_id_metadata(id_league integer, "round" integer)
RETURNS varchar(20) IMMUTABLE
AS $$
BEGIN
    RETURN id_league || '-' || "round";
END;
$$ LANGUAGE plpgsql;

create table if not exists ftd.metadata (
	id serial,
	id_league integer not null,
	"round" integer not null,
	status varchar(13),
	updated_at timestamp default current_timestamp,
	id_compost varchar(20) unique generated always as (generate_compost_id_metadata(id_league, "round")) stored,
	constraint metadata_pk primary key (id),
	constraint metadata_league_fk foreign key (id_league) references "ftd".leagues (id)
);

CREATE TRIGGER trigger_att_updated_at_metadata
BEFORE INSERT OR UPDATE ON ftd.metadata
FOR EACH ROW
EXECUTE FUNCTION updated_at_with_current_timestamp();