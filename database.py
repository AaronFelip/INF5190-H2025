import hashlib
import os
import sqlite3
import random
import uuid
from datetime import date


def get_avatar_aleatoire():
    avatar = ['anime.png', 'batman.png', 'bear-russia.png', 'coffee.png', 'jason.png', 'zombie.png']
    return random.choice(avatar)


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


    def creer_utilisateur(self, nom, prenom, courriel, mdp):
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(str(mdp + salt).encode("utf-8")).hexdigest()
        date_inscription = date.today()
        connection = self.get_connection()
        avatar_par_default = get_avatar_aleatoire()
        connection.execute(
            "INSERT INTO utilisateur(nom, prenom, courriel, date_inscription, avatar_id, mot_de_passe_salt, mot_de_passe_hash) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (nom, prenom, courriel, date_inscription, avatar_par_default, salt, hashed_password)
        )
        connection.commit()


        # Dans la classe Database
    def verifier_utilisateur(self, courriel, mdp):
        """Vérifie les credentials de l'utilisateur et retourne ses données si valides."""
        connection = self.get_connection()
        cursor = connection.cursor()
        try:
            # Récupère le salt et le hash stockés
            cursor.execute(
                "SELECT id, nom, prenom, mot_de_passe_salt, mot_de_passe_hash "
                "FROM utilisateur WHERE courriel = ?",
                (courriel,)
            )
            user = cursor.fetchone()

            if user:
                user_id, nom, prenom, salt, stored_hash = user
                # Génère le hash avec le mot de passe fourni et le salt stocké
                hashed_password = hashlib.sha512(
                    str(mdp + salt).encode("utf-8")
                ).hexdigest()

                # Vérifie si les hashs correspondent
                if hashed_password == stored_hash:
                    return {
                        'id': user_id,
                        'nom': nom,
                        'prenom': prenom,
                        'courriel': courriel
                    }
        finally:
            cursor.close()
        return None



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

