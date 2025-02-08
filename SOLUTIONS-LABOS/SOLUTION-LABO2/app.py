from flask import Flask, render_template, redirect, url_for, request
import os
import markdown
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/labo2', methods=['GET', 'POST'])
def labo2():
    # Définir le titre de la page
    title = "Laboratoire 2"

    # Gestion des requêtes GET
    if request.method == 'GET':
        # Retourner le formulaire initial avec le titre
        return render_template('labo2.html', title=title), 200

    # Gestion des requêtes POST
    # Récupérer les données envoyées dans le formulaire
    form_data = {
        'nom': request.form.get('nom', "").strip(),       # Nom de l'utilisateur
        'prenom': request.form.get('prenom', "").strip(), # Prénom de l'utilisateur
        'age': request.form.get('age', "").strip()        # Âge de l'utilisateur
    }

    # Vérifier si tous les champs ont été remplis
    if not all(form_data.values()):
        erreur = "Tous les champs doivent être remplis"
        # Retourner le formulaire avec un message d'erreur et les données déjà saisies
        return render_template('labo2.html', erreur=erreur, **form_data, title=title)

    # Écriture des données dans le fichier de log
    log_data = f"{form_data['nom']}, {form_data['prenom']}, {form_data['age']}\n"
    with open("log-labo2.txt", 'a', encoding="utf8") as log:
        log.write(log_data)

    # Redirection vers la page de confirmation
    return redirect(url_for('confirmation'), 302)


@app.route("/labo2/liste")
def liste_labo2():
    # Liste pour stocker les données extraites du fichier de log
    liste_membres = []
    chemin_fichier_log = "log-labo2.txt"

    try:
        # Ouvrir le fichier de log en mode lecture
        with open(chemin_fichier_log, 'r', encoding="utf8") as fichier_log:
            lignes_log = fichier_log.readlines()

        # Parcourir chaque ligne du fichier et extraire les informations
        for ligne in lignes_log:
            informations_membre = ligne.strip().split(", ")  # Découper la ligne en utilisant ", " comme séparateur
            liste_membres.append(informations_membre)  # Ajouter les données extraites à la liste

    except FileNotFoundError:
        # Gérer le cas où le fichier de log n'existe pas
        return render_template(
            "labo2-liste.html",
            resultats=None,
            message="Il n'y a pas de nouveau membre pour le moment."
        ), 200

    # Vérifier si le fichier existe mais est vide
    if not liste_membres:
        return render_template(
            "labo2-liste.html",
            resultats=None,
            message="Il n'y a pas de nouveau membre pour le moment."
        ), 200

    # Si des membres sont trouvés, les transmettre au template
    return render_template(
        "labo2-liste.html",
        resultats=liste_membres,
        message=None,
        len=len(liste_membres)
    ), 200


@app.route('/confirmation', methods=['GET'])
def confirmation():
    title = "Confirmation"
    return render_template('confirmation.html',
                           title=title), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run()
