from flask import Flask, render_template,request, g, url_for, redirect
from database import Database
from datetime import date
import re
import hashlib
import uuid
import secrets



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()




regex = r"[A-Za-z0-9#$%&'*+/=?@]{8,}" #possiblement incomplet
mdp_existant = re.compile(regex).match


def get_db():
    database = getattr(g, "_database", None)
    if database is None:
        g._database = Database()
    return g._database


def close_connection():
    database = getattr(g, "_database", None)
    if database is not None:
        database.deconnection()

def courriel_existe(courriel):
    return get_db().courriel_existe(courriel)

def valider_courriel(courriel, validation_courriel):
    return courriel == validation_courriel

def valider_mdp(str):
    try:
        if mdp_existant(str) is not None:
            return True
    except:
        pass
    return False


@app.route('/', methods=['GET', 'POST'])
def home():
    title = "Mon site - veuillez vous sinscrire"
    if request.method == "GET":
        return render_template("index.html", title=title), 200
    else:

        nom = request.form['nom']
        prenom = request.form['prenom']
        courriel = request.form['courriel']
        validation_courriel = request.form['validation-courriel']
        mdp = request.form['mdp']

        if (nom == "" or prenom == "" or courriel == "" or validation_courriel == "" or mdp == ""):
            message_erreur = "Erreur, tous les champs doivent être remplis"
            return render_template("index.html", title=title,
                                   message_erreur=message_erreur,
                                   nom=nom, prenom=prenom, courriel=courriel), 400

        if courriel_existe(courriel):
            courriel_erreur = "Ce courriel existe deja"
            return render_template("index.html",
                                   title=title, courriel_erreur=courriel_erreur,
                                   nom=nom, prenom=prenom, courriel=courriel), 400


        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(str(mdp + salt).encode("utf-8")).hexdigest()
        date_inscription = date.today()
        get_db().inserer_utilisateur(nom, prenom, courriel, date_inscription, salt, hashed_password)
        return redirect(url_for("confirmation")), 302