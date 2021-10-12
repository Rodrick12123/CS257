#Tables
CREATE TABLE athlete_events (
    id integer,
    name text,
    sex text,
    age integer,
    height integer,
    weight integer,
    team text,
    NOC text,
    games text,
    year integer,
    season text,
    city text,
    sport text,
    event text,
    medal text
);

CREATE TABLE noc_regions (
  id integer,
  region text,
  notes text
);
