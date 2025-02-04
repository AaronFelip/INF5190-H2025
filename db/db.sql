CREATE TABLE utilisateur (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    courriel TEXT,
    date_inscription date,
    avatar_id varchar(32),
    mot_de_passe_hash TEXT NON NULL,
    mot_de_passe_salt TEXT NON NULL
);

CREATE TABLE avatar(
   id VARCHAR(32) primary key,
   data blob
);