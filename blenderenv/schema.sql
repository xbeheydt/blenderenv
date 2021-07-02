DROP TABLE IF EXISTS release_type;
CREATE TABLE release_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

INSERT INTO release_type (name)
VALUES
    ('all'),
    ('prebuilt'),
    ("source");

DROP TABLE IF EXISTS release;
CREATE TABLE release (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type INTEGER NOT NULL,
    version TEXT NOT NULL,
    url TEXT UNIQUE NOT NULL,
    FOREIGN KEY (type) REFERENCES release_type (id)
);

DROP TABLE IF EXISTS installed;
CREATE TABLE installed (
    id INTEGER PRIMARY KEY NOT NULL,
    FOREIGN KEY (id) REFERENCES release (id)
        ON DELETE CASCADE ON UPDATE NO ACTION
);
