CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 5ed4892f165b

CREATE TABLE codigo_bipado (
    id INTEGER NOT NULL, 
    codigo_barra VARCHAR(250), 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('5ed4892f165b') RETURNING version_num;

