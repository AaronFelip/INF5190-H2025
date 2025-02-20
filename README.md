## À propos:
Ce dépot contient les corrections des labos du groupe 10, n'hésitez pas à le consulter
pour vos travaux pratiques.  
**Je push la correction du labo en cours au plus tard le matin du laboratoire suivant. Il est possible que
la solution de certains labos ne soient pas disponibles à des fins de consultations ultérieurs.
Votre présence aux laboratoires est le meilleur moyen d'avoir les réponses aux solutions.**

## Laboratoires:
- Semaine 1: Pas de labo cette semaine
- Semaine 2: Labo 1 - [Introduction à Flask](/SOLUTIONS-LABOS/SOLUTION-LABO1)
- Semaine 3: Labo 2 - [Flask suite](/SOLUTIONS-LABOS/SOLUTION-LABO2)
- Semaine 3: Labo 2.5 - [Python et Sqlite3](/SOLUTIONS-LABOS/SOLUTION-LABO2-SQLITE3)
- Semaine 4: Labo 3 - [Flask et Sqlite3](/SOLUTIONS-LABOS/SOLUTION-LABO3)
- Semaine 5: Labo 4 - Sessions (aucune solution pour ce labo)
- Semaine 6: Labo 5 - JSON et XML (aucune solution pour ce labo)
- Semaine 7: Labo 6 - [Premier API](/SOLUTIONS-LABOS/SOLUTION-LABO6)
- Semaine 8: à venir
- Semaine 9: à venir
- Semaine 10: à venir
- Semaine 11: à venir
- Semaine 12: à venir
- Semaine 13: à venir
- Semaine 14: à venir
- Semaine 15: à venir

## Me rejoindre:
Si vous avez des questions sur la matière vu en classe ou dans les labos,
je vous recommande de poser vos questions dans le Discord du cours.
L'un de vos camarades vous répondra, autrement si vous avez besoin d'une
aide personnalisée, vous pouvez me rejoindre par
[courriel](mailto:osorio_arancibia.aaron@courrier.uqam.ca?subject=Aide%20labo%20INF5190).



## Comment utiliser le logiciel:
Voici un guide complet pour cloner, configurer et exécuter le projet Flask `INF5190-H2025` sur Windows, macOS et 
Linux en utilisant Visual Studio Code (VS Code) ou PyCharm.

---

### **1. Cloner le projet depuis GitHub**
#### Commandes Git :
1. **Cloner le projet dans un répertoire local** :
  - Ouvrez un terminal ou une console.
  - Exécutez la commande suivante pour cloner le dépôt :
    ```bash
    git clone git@github.com:AaronFelip/INF5190-H2025.git
    ```

2. **Accéder au répertoire cloné** :
   ```bash
   cd INF5190-H2025
   ```

---

### **2. Installer les prérequis**
Le projet contient un fichier `requirements.txt` listant les dépendances nécessaires pour exécuter le projet. 
Ces dépendances devraient se télécharger et s'installer d'elles-mêmes lors de l'ouverture de votre IDE. Dans un cas
contraire, portez attention à ce fichier (voir plus bas).

#### Étapes pour Windows, macOS et Linux :
1. **Vérifier que Python est installé** :
  - Exécutez la commande suivante pour vérifier la version de Python :
    ```bash
    python --version
    ```
  - Sur certaines distributions Linux et macOS, utilisez `python3` au lieu de `python`.

  - Si Python n'est pas installé :
    - **Windows** : Téléchargez [Python](https://www.python.org/downloads/) et installez-le en cochant l'option 
    "Add Python to PATH" pendant l'installation.
    - **macOS/Linux** : Utilisez le gestionnaire de paquets de votre système :
      ```bash
      sudo apt install python3 python3-pip  # Ubuntu/Debian
      brew install python                  # macOS avec Homebrew
      ```

2. **Installer `pip` (gestionnaire de paquets Python)** :
  - La plupart des distributions Python incluent déjà `pip`. Pour vérifier :
    ```bash
    pip --version
    ```
  - Si `pip` n'est pas installé, utilisez :
    - **Windows** :
      ```bash
      python -m ensurepip --upgrade
      ```
    - **macOS/Linux** :
      ```bash
      python3 -m ensurepip --upgrade
      ```

  
#### **3. Créer un environnement virtuel**
Un environnement virtuel permet d'isoler les dépendances spécifiques d'un projet Python. Voici les étapes :

1. **Placez-vous dans le répertoire du projet Flask** :
  - Après avoir cloné le dépôt GitHub, placez-vous dans le dossier du projet :
    ```bash
    cd INF5190-H2025
    ```

2. **Créer l'environnement virtuel à la racine du projet** :
  - Exécutez la commande suivante dans le répertoire du projet pour créer un environnement virtuel nommé `.venv` :
    ```bash
    python -m venv .venv
    ```
  - Cela créera un dossier `.venv` à la racine, où seront installées toutes les dépendances nécessaires.

3. **Activer l'environnement virtuel** :
  - Une fois l'environnement créé, activez-le pour utiliser les dépendances dans cet environnement isolé.

  - **Sous Windows** :
    ```bash
    .venv\Scripts\activate
    ```
  - **Sous macOS/Linux** :
    ```bash
    source .venv/bin/activate
    ```

4. **Confirmer l'activation** :
  - Vous saurez que l'environnement virtuel est activé si le nom de l'environnement (par exemple, `.venv`) apparaît dans le terminal. Exemple :
    ```
    (.venv) C:\Users\VotreNom\INF5190-H2025>
    ```

5. **Installer les dépendances** :
  - Une fois l'environnement activé, installez les dépendances listées dans `requirements.txt` :
    ```bash
    pip install -r requirements.txt
    ```
  - Cela installe toutes les bibliothèques nécessaires pour exécuter le projet Flask dans l'environnement virtuel.

---

### **3. Configurer l'exécution du projet**
#### Étapes pour tous les systèmes :
1. **Vérifiez que le fichier principal du projet (`app.py` ou similaire) est présent**.
2. **Configurer les variables d'environnement Flask** :
  - Sous Windows (dans cmd) :
    ```bash
    set FLASK_APP="app.py"
    set FLASK_ENV="development"
    set FLASK_DEBUG=1
    ```
  - Sous macOS/Linux :
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    ```

3. **Lancer l’application** :
  - Utilisez la commande Flask suivante pour démarrer le serveur :
    ```bash
    flask run
    ```
  - Le serveur sera accessible à l'adresse suivante :
    - [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### **4. Utilisation avec VS Code ou PyCharm**

#### **VS Code** :
1. **Ouvrir le projet dans VS Code** :
  - Dans le terminal, lancez :
    ```bash
    code .
    ```

2. **Configurer l’interpréteur Python** :
  - Cliquez sur l'icône en bas à droite pour sélectionner l'interpréteur Python.
  - Choisissez l’environnement virtuel `.venv` créé.

3. **Exécuter l’application Flask** :
  - Ouvrez le terminal intégré (`Ctrl + \` ou `Ctrl + Shift + \` sur macOS).
  - Activez l’environnement virtuel :
    - **Windows** : `.venv\Scripts\activate`
    - **macOS/Linux** : `source .venv/bin/activate`
  - Lancez le projet avec `flask run`.

#### **PyCharm** :
1. **Ouvrir le projet dans PyCharm**.
2. **Configurer l’interpréteur Python** :
  - Allez dans `File > Settings > Python Interpreter`.
  - Ajoutez l’environnement virtuel `.venv`.
3. **Créer une configuration Flask** :
  - Allez dans `Run > Edit Configurations`.
  - Cliquez sur le `+` et choisissez `Flask`.
  - Configurez :
    - **Target** : `app.py` (ou le fichier principal).
    - **Environment Variables** : Ajoutez `FLASK_APP=app.py` et `FLASK_ENV=development`.
  - Enregistrez et exécutez.

---

### **5. Gestion des modifications**
#### Forker le projet :
1. **Fork sur GitHub** :
  - Rendez-vous sur la page du dépôt : [INF5190-H2025](https://github.com/AaronFelip/INF5190-H2025).
  - Cliquez sur le bouton **Fork**.

2. **Cloner votre fork** :
  - Clonez votre propre version :
    ```bash
    git clone git@github.com:<VotreNomUtilisateur>/INF5190-H2025.git
    ```

3. **Créer une branche pour les modifications** :
  - Avant de modifier, créez une nouvelle branche :
    ```bash
    git checkout -b votre-branche
    ```

4. **Pusher vos changements sur votre fork** :
  - Une fois les modifications faites :
    ```bash
    git add .
    git commit -m "Vos modifications"
    git push origin votre-branche
    ```

#### Mise à jour du projet original :
- Si le projet original est mis à jour après les laboratoires, vous pouvez récupérer les dernières modifications en 
réinitialisant votre fork :
  ```bash
  git remote add upstream git@github.com:AaronFelip/INF5190-H2025.git
  git pull upstream main
  ```

---

### **6. Notes importantes**
- **Liberté d’utilisation** :
  - Ce projet est libre de droits. Vous pouvez le modifier, le redistribuer et l'utiliser comme bon vous semble.
  - Dans le cadre de vos évalutations, utiliser le design du site tel quel, pourrait être vu comme un manque d'effort
  et vous couter des points.
- **Recommandation** :
  - Travaillez toujours sur une branche spécifique dans votre fork pour éviter des conflits lorsque vous récupérez 
  les mises à jour.
- **Mise à jour** :
  - Ce projet sera mis à jour régulièrement après les laboratoires. Recommencez la procédure pour synchroniser votre 
  copie locale avec la dernière version.

---

Avec ce guide, vous êtes prêt à cloner, configurer et lancer le projet sur Windows, macOS ou Linux ! Si vous 
avez des questions, n'hésitez pas. 😊


## Liens utiles:
- [Validateur du W3C pour le html](https://validator.w3.org/)
- [Validateur du W3C pour le css](https://jigsaw.w3.org/css-validator/)
- [Bootstrap](https://getbootstrap.com/)
- [Documentation de Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Télécharger Python](https://www.python.org/downloads/)
- [IDE PyCharm - gratuit pour les étudiants](https://www.jetbrains.com/pycharm/)
  &nbsp;  
  &nbsp;

> [!NOTE]
> License Apache 2.0 - Vous êtes libres d'utiliser, modifier et distribuer mon code, tant que vous citez © l'auteur 
> original, c'est-à-dire moi ou votre prof s'il a été fourni par ce dernier.