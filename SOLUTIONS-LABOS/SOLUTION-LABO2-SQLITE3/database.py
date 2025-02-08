import sqlite3

class Database:
    """
    Classe pour gérer les opérations sur la base de données musique.
    """

    def __init__(self):
        """
        Initialise une connexion à None.
        """
        self.connection = None

    def get_connection(self):
        """
        Établit une connexion avec la base de données si elle n'existe pas encore.
        Retourne l'objet connexion.
        """
        if self.connection is None:
            self.connection = sqlite3.connect("db/musique.db")
        return self.connection

    def disconnect(self):
        """
        Ferme la connexion à la base de données si elle est ouverte.
        """
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_all_artistes(self):
        """
        Affiche tous les artistes enregistrés dans la table 'artiste'.
        """
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT id, nom, est_solo, nombre_individus FROM artiste")
        for row in cursor:
            identifier, nom, est_solo, nombre_individus = row
            print(f"ID : {identifier}, Nom : {nom}, Solo : {'Oui' if est_solo else 'Non'}, Membres : {nombre_individus}")

    def get_album_artiste(self, artiste_id):
        """
        Affiche tous les albums d'un artiste spécifique donné par son ID.
        """
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT titre, annee FROM album WHERE artiste_id = ?", (artiste_id,))
        for row in cursor:
            titre, annee = row
            print(f"Album : {titre}, Année : {annee}")

    def insert_album(self, nom_artiste, nom_album, annee):
        """
        Insère un nouvel album dans la table 'album'.
        Si l'artiste n'existe pas, il est ajouté dans la table 'artiste'.
        """
        connection = self.get_connection()
        cursor = connection.cursor()

        # Vérifier si l'artiste existe
        cursor.execute("SELECT id FROM artiste WHERE nom = ?", (nom_artiste,))
        artiste = cursor.fetchone()

        if artiste:
            artiste_id = artiste[0]
        else:
            # Ajouter l'artiste s'il n'existe pas
            cursor.execute(
                "INSERT INTO artiste (nom, est_solo, nombre_individus) VALUES (?, ?, ?)",
                (nom_artiste, 0, 1)  # Par défaut, l'artiste ajouté est un groupe avec 1 membre
            )
            connection.commit()
            artiste_id = cursor.lastrowid

        # Ajouter l'album dans la base
        cursor.execute(
            "INSERT INTO album (titre, annee, artiste_id, maison_disque_id) VALUES (?, ?, ?, ?)",
            (nom_album, annee, artiste_id, None)  # Par défaut, maison_disque_id est NULL
        )
        connection.commit()
        print(f"Album '{nom_album}' ajouté avec succès pour l'artiste '{nom_artiste}'.")

