#Tables
CREATE TABLE athletes (
    id integer,
    firstname text,
    lastname text,
    sex text

);

CREATE TABLE events (
    athleteid integer,
    age integer,
    height integer,
    weight float,
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
  region text,
  gold_medal integer
);
#list
\copy noc_regions FROM 'noc.csv' DELIMITER ',' CSV NULL AS 'NULL'
SELECT * FROM noc_regions
ORDER BY noc_regions.NOC;

\copy athletes FROM 'athlete.csv' DELIMITER ',' CSV NULL AS 'NULL'
\copy events FROM 'event.csv' DELIMITER ',' CSV NULL AS 'NULL'
SELECT athletes.firstname, athletes.lastname
FROM athletes, events
WHERE athletes.id = events.athleteid
AND events.team LIKE 'Kenya%'
ORDER BY lastname;

SELECT athletes.firstname, athletes.lastname, events.medal
FROM athletes, events
WHERE athletes.id = events.athleteid
AND athletes.lastname LIKE 'Louganis%'
AND athletes.firstname LIKE 'Greg%'
ORDER BY year;

SELECT noc_regions.NOC, noc_regions.gold_medal
FROM noc_regions
ORDER BY gold_medal DESC;

SELECT * FROM events
ORDER BY noc_regions.NOC;
