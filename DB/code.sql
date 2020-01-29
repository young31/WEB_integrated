DROP TABLE classmates;

CREATE TABLE classmates(
    -- id INT PRIMARY KEY,
    name TEXT,
    age INT,
    address TEXT
);

INSERT INTO classmates (name, age)
    VALUES ('name', 19);

INSERT INTO classmates (name, age, address)
    VALUES ('json', 30, 'Seoul');

SELECT rowid, name FROM classmates;


nullvalue ‘NULL’ sqlite> CREATE TABLE ssafy ( …> id INTEGER PRIMARY KEY, …> location TEXT, …> class INTEGER …> ); sqlite> INSERT INTO ssafy (id, location) …> VALUES (1, ‘JEJU’); sqlite> SELECT class FROM ssafy WHERE id=1;

INSERT INTO bands
VALUES (1, 'Queen', 1973), (2, 'Coldplay', 1998), (3, 'MCR', 2001);

SELECT id, name FROM bands;


SELECT * FROM users ORDER BY age, last_name LIMIT 10;

SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;

CREATE TABLE articles (
    title TEXT NOT NULL,
    content TEXT NOT NULL
    );

INSERT INTO articles
    VALUES ('first', 'json handsome');

ALTER TABLE articles RENAME to news;

ALTER TABLE news ADD COLUMN created_at DATETIME;

INSERT INTO news
    VALUES ('title', 'content', datetime('now', 'localtime'));


ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;



CREATE TABLE friends(
    id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT
    );

INSERT INTO friends
 VALUES (1, 'Justin', 'Seoul'), (2, 'Simon', 'New York'), (3, 'Chang', 'Las Vegas'), (4, 'John', 'Sydney');

 ALTER TABLE friends ADD COLUMN married INTEGER;

INSERT INTO friends (location, married)
    VALUES ('LA', 1), ('New York', 0), ('LasVegas', 0), ('Sydney', 1);

CREATE TABLE bands(
    id INTEGER PRIMARY KEY,
    name TEXT,
    dedut INTEGER);

INSERT INTO bands
    VALUES (1, 'Queen', 1973), (2, 'Coldplay', 1998), (3, 'MCR', 2001);


ALTER TABLE bands ADD COLUMN members INTEGER;

INSERT INTO bands (members)
    VALUES (4), (5), (9);


DELETE FROM bands WHERE rowid=2;

UPDATE bands SET members=5 WHERE rowid=1;