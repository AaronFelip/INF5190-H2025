import sqlite3

class Database():

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db')
        return self.connection


    def close_connection(self):
        if self.connection is not None:
            self.connection.close()


    def inserer_utilisateur(self, nom, prenom, courriel, date_inscription, salt, hashed_password):
        connection = self.get_connection()
        connection.execute(
            "INSERT INTO utilisateur(nom, prenom, courriel, date_inscription, mot_de_passe_salt, mot_de_passe_hash) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (nom, prenom, courriel, date_inscription, salt, hashed_password)
        )
        connection.commit()

    def courriel_existe(self, courriel):
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT 1 FROM utilisateur WHERE courriel = ?", (courriel,))
            return cursor.fetchone() is not None
        finally:
            cursor.close()
