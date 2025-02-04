import os
import sqlite3
import random
import uuid


def get_random_default_avatar():
    avatar_dir = os.path.join('static', 'images', 'def-avatar')
    avatar_files = ['anime.png', 'batman.png', 'bear-russia.png', 'coffee.png', 'jason.png', 'zombie.png']
    return random.choice(avatar_files)



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


    def creer_utlisateur(self, nom, prenom, courriel, date_inscription, salt, hashed_password):
        connection = self.get_connection()

        # Générer un avatar par défaut
        default_avatar = get_random_default_avatar()
        connection.execute(
            "INSERT INTO utilisateur(nom, prenom, courriel, date_inscription, avatar_id, mot_de_passe_salt, mot_de_passe_hash) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (nom, prenom, courriel, date_inscription, default_avatar, salt, hashed_password)
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


    # Avatar management
    def mettre_avatar_a_jour(self, user_id, avatar_data):
        connection = self.get_connection()
        cursor = connection.cursor()
        avatar_id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO avatar (id, data) VALUES (?, ?)",
            (avatar_id, avatar_data)
        )
        cursor.execute(
            "UPDATE user SET avatar_id = ? WHERE id = ?",
            (avatar_id, user_id)
        )
        connection.commit()
        return avatar_id

    def charger_avatar(self, avatar_id):
        if avatar_id in ['anime.png', 'batman.png', 'bear-russia.png', 'coffee.png', 'jason.png', 'zombie.png']:
            avatar_path = os.path.join('static', 'images', 'def-avatar', avatar_id)
            with open(avatar_path, 'rb') as f:
                return f.read()
        else:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT data FROM avatar WHERE id = ?", (avatar_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
        return None

