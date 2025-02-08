from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/labo1', methods=['GET', 'POST'])
def labo1():
    # Définir le titre de la page
    title = "Laboratoire 1"

    # Gestion des requêtes GET
    if request.method == 'GET':
        # Renvoyer le formulaire vide avec les paramètres par défaut
        return render_template('labo1.html',
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
        return render_template('labo1.html',
                               erreur=erreur,
                               username=form_data['username'],
                               title=title), 400

    # Écriture des données dans un fichier de log
    log_data = (
        f"Nom d'utilisateur : {form_data['username']}\n"
        f"Option : {form_data['option']}\n"
        f"Choix : {form_data['select']}\n"
    )
    with open('log-labo1.txt', 'w') as log:
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


if __name__ == '__main__':
    app.run()
