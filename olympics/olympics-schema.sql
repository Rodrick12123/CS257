#Tables
CREATE TABLE athletes (
    id integer,
    firstname text,
    lastname text,
    sex text,
    age integer,
    height integer,
    weight float
);

CREATE TABLE events (
    athleteid integer,
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
  NOC text,
  region text
);
#list
\copy noc_regions FROM 'noc.csv' DELIMITER ',' CSV NULL AS 'NULL'
SELECT * FROM noc_regions
ORDER BY noc_regions.NOC;

\copy athletes FROM 'athlete.csv' DELIMITER ',' CSV NULL AS 'NULL'
\copy athletes FROM 'athlete.csv' DELIMITER ',' CSV NULL AS 'NULL'
SELECT athletes.firstname, athletes.lastname
FROM athletes, events
WHERE athletes.id = events.athleteid
AND events.city LIKE 'c'
ORDER BY lastname;

\copy events FROM 'events.csv' DELIMITER ',' CSV NULL AS 'NULL'
SELECT * FROM events
ORDER BY noc_regions.NOC;
