from database import Database

# Initialiser une instance de la classe Database
db = Database()

def lire_db():
    # Récupérer et afficher tous les artistes
    artistes = db.get_all_artistes()
    print("Liste des artistes disponibles :")
    for artiste in artistes:
        print(f"ID : {artiste['id']}, Nom : {artiste['nom']}")

    # Demander à l'utilisateur de choisir un artiste par son ID
    print("Choisissez un artiste en entrant son ID :")
    try:
        choix_id = int(input("ID de l'artiste : "))

        # Afficher les albums de l'artiste sélectionné
        albums = db.get_album_artiste(choix_id)

        if albums:
            print(f"Albums pour l'artiste ID {choix_id} :")
            for album in albums:
                print(f"- {album['titre']} ({album['annee']})")
        else:
            print(f"Aucun album trouvé pour l'artiste ID {choix_id}.")
    except ValueError:
        print("Erreur : vous devez entrer un ID valide.")

def ecrire_db():
    try:
        # Ouvrir le fichier contenant les données d'albums
        with open("input.txt", "r") as fichier_entree:
            for ligne in fichier_entree:
                # Diviser chaque ligne en parties : titre, artiste, année
                titre, artiste, annee = ligne.strip().split('|')
                # Insérer les données dans la base
                db.insert_album(titre, artiste, annee)
        print("Les albums ont été ajoutés avec succès à la base de données.")
    except FileNotFoundError:
        print("Erreur : le fichier 'input.txt' est introuvable.")
    except ValueError:
        print("Erreur : une ligne du fichier n'est pas correctement formatée.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    """
    Point d'entrée du script :
    - Ajouter des albums à la base de données depuis un fichier texte.
    - Permettre à l'utilisateur de lire les artistes et leurs albums.
    """
    # Ajouter les albums dans la base de données
    ecrire_db()
    # Lire et afficher les artistes et albums
    lire_db()
    # Fermer la connexion à la base de données
    db.disconnect()
