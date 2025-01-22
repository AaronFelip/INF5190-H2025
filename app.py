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
