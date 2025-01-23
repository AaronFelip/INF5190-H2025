from flask import Flask, render_template, redirect, url_for, request
import os
import markdown
app = Flask(__name__, static_url_path='', static_folder='static')

ENONCES_DIR = 'enonces'  # Dossier contenant les énoncés, vous l'effacez,
# vous mourrez 💀


@app.route('/labo1', methods=['GET', 'POST'])
def labo1():
    # Définir le titre de la page
    title = "Laboratoire 1"

    # Gestion des requêtes GET
    if request.method == 'GET':
        # Renvoyer le formulaire vide avec les paramètres par défaut
        return render_template('labos/labo1.html',
                               username="",
                               erreur="",
                               title=title), 200

    # Gestion des requêtes POST
    # Récupérer les données du formulaire en s'assurant qu'elles ne
    # sont pas nulles
    form_data = {
        'username': request.form['username'].strip(),
        'option': request.form.get('option', "").strip(),
        'select': request.form.get('select', "").strip()
    }

    # Vérifier si tous les champs du formulaire ont été remplis
    if not all(form_data.values()):
        erreur = "Tous les champs du formulaire doivent être remplis."
        # Renvoyer le formulaire avec un message d'erreur et les valeurs
        # déjà saisies
        return render_template('labos/labo1.html',
                               erreur=erreur,
                               username=form_data['username'],
                               title=title), 400

    # Écriture des données dans un fichier de log
    log_data = (
        f"Nom d'utilisateur : {form_data['username']}\n"
        f"Option : {form_data['option']}\n"
        f"Choix : {form_data['select']}\n"
    )
    with open('logs-db/log-labo1.txt', 'w') as log:
        log.write(log_data)

    # Rediriger l'utilisateur vers la page de confirmation
    return redirect(url_for('confirmation'), 302)


@app.route('/labo2', methods=['GET', 'POST'])
def labo2():
    # Définir le titre de la page
    title = "Laboratoire 2"

    # Gestion des requêtes GET
    if request.method == 'GET':
        # Retourner le formulaire initial avec le titre
        return render_template('labos/labo2.html', title=title), 200

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
        return render_template('labos/labo2.html', erreur=erreur, **form_data, title=title)

    # Écriture des données dans le fichier de log
    log_data = f"{form_data['nom']}, {form_data['prenom']}, {form_data['age']}\n"
    with open("logs-db/log-labo2.txt", 'a', encoding="utf8") as log:
        log.write(log_data)

    # Redirection vers la page de confirmation
    return redirect(url_for('confirmation'), 302)


@app.route("/labo2/liste")
def liste_labo2():
    # Liste pour stocker les données extraites du fichier de log
    liste_membres = []
    chemin_fichier_log = "logs-db/log-labo2.txt"

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
            "labos/labo2-liste.html",
            resultats=None,
            message="Il n'y a pas de nouveau membre pour le moment."
        ), 200

    # Vérifier si le fichier existe mais est vide
    if not liste_membres:
        return render_template(
            "labos/labo2-liste.html",
            resultats=None,
            message="Il n'y a pas de nouveau membre pour le moment."
        ), 200

    # Si des membres sont trouvés, les transmettre au template
    return render_template(
        "labos/labo2-liste.html",
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

##########################################################################
#                                                                        #
#           ROUTES POUR LE BON FONCTIONNEMENT DU SITE WEB                #
#                                                                        #
#  Les routes et fonctions définies ci-dessous permettent d'assurer les  #
#  fonctionnalités principales de l'application                          #
#                                                                        #
#                                                                        #
##########################################################################


@app.route('/')
def index():
    """Affiche les énoncés sous forme de fiches."""
    title = "INF5190 PROJET SESSION"
    enonces = []
    try:
        for filename in os.listdir(ENONCES_DIR):
            if filename.endswith('.md'):
                filepath = os.path.join(ENONCES_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Limiter la longueur du contenu pour le thumbnail
                    preview = markdown.markdown(content[:140]) + "..."
                    enonces.append({
                        'name': filename,
                        'title': filename.replace('.md', '').capitalize(),
                        'preview': preview
                    })
    except FileNotFoundError:
        pass

    while len(enonces) < 10:
        enonces.append({
            'name': None,
            'title': "Énoncé à venir",
            'preview': "Le contenu de cet énoncé sera disponible "
                       "prochainement."
        })

    return render_template('index.html',
                           title=title,
                           enonces=enonces), 200


@app.route('/enonce/<filename>')
def show_enonce(filename):
    """Afficher le contenu Markdown d'un énoncé."""
    filepath = os.path.join(ENONCES_DIR, filename)
    if not os.path.exists(filepath):
        return "Énoncé introuvable.", 404
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content = markdown.markdown(content)
    return render_template('enonce.html',
                           content=html_content,
                           title=filename.replace('.md', '').capitalize()), 200


@app.context_processor
def inject_enonces():
    """Injecte la liste des énoncés dans les templates."""
    try:
        files = [f for f in os.listdir(ENONCES_DIR) if f.endswith('.md')]
        enonces = [
            {'name': f, 'title': f.replace('.md', '').
                capitalize()} for f in files
        ]
        return {'enonces': enonces}
    except FileNotFoundError:
        return {'enonces': []}


if __name__ == '__main__':
    app.run()
