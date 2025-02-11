### **Résumé des rappels importants**

Pour ce projet, vous devez utiliser **Flask** et **SQLite3** pour la partie backend.  (obviously)

#### **Base de données :**
- Pour lancer votre première base de données SQLite3 :
  ```sh
  sqlite3 database.db
  ```
- Pour exécuter un script SQL dans SQLite3 :
  ```sh
  .read fichier.sql
  ```

#### **Frontend :**
- **HTML / CSS** suffisent amplement.
- **Ne perdez pas de temps** sur le design, la note est minime pour cette partie mais faites pas quelque chose de dégeu non plus parce que c'est tout de même à l'appréciation du correcteur-trice.
- **Si vous ne connaissez pas Bootstrap, jQuery ou Underscore.js, ne les utilisez pas.**

#### **Navigation et qualité du code :**
- **La navigation entre les 5 pages du TP doit être fluide et impeccable.**
- **Le code HTML, CSS, JS et Python doit être valide.**
- **Respectez les conventions de nommage :**
    - **HTML** : `une-page.html` (kebab-case)
    - **CSS** : `un-selecteur`, `une-classe`, ou **BEM** (`navigation__menu`, `nav__items`)
    - **Python** : `une_fonction`, `une_variable`, `Une_Classe`
    - **JavaScript** : `uneFonction`, `UneClasse`, `uneVariable`

#### **Commentaires et structuration :**
- **Votre code doit être commenté.**
- Exemple de docstring en Python :
  ```python
  def ma_fonction(param):
      """
      Description de la fonction.
      
      :param param: Description du paramètre.
      :return: Description de la valeur de retour.
      """
      return param
  ```
- **Si vous codez en français, tout le code doit être en français.**
- **Si vous codez en anglais, tout le code doit être en anglais.**

---

### **Erreurs fréquentes qui vous feront perdre des points :**

1. **Votre code Python ne passe pas PEP 8 (`pycodestyle`).**
2. **Vous ne respectez pas les noms de routes spécifiés.**
3. **Vous importez des librairies non autorisées.**
4. **Erreurs de validation HTML / CSS avec w3c.**
5. **Aucune validation de la longueur des entrées utilisateur avant insertion en BD.**
6. **Code illisible et non explicite (ex. `let liste` au lieu de `let liste_utilisateurs_actifs`, ou `def route1():` au lieu de `def page_not_found():`).**
7. **Mauvaise organisation des fichiers (`utils/`, `models/`, `static/css/`, etc.).**
8. **Absence du fichier `requirements.txt`.**
9. **Oubli des codes de retour HTTP (`return jsonify(...), 200` par ex.).**
10. **Votre site n'est pas en UTF-8 ou n'a pas `lang="fr"` dans le HTML.**
11. **Pas d'utilisation de placeholders SQL (`?`) .**
12. **Stockage d’informations sensibles dans les variables de session (`salt`, `hash`).**
13. **Site inutilisable bien qu'il fonctionne chez vous (ex. chemins absolus, bugs non anticipés).**
14. **Menus de navigation absents sur certaines pages.**
15. **Utilisation d'un template.**
16. **Utilisation abusive d’une stack trop lourde pour aucune fucking raison, comme :** **
- **React** pour afficher un compteur de clics.
- **Algolia** pour faire une recherche dans une table de 10 utilisateurs.
- **Tailwind** pour styliser un `<h1>` en bleu.
- **TypeScript** pour valider un champ texte de 20 caractères.
17. **Vous oublirez de nommer votre fichier selon votre code permanent...**

Voilà j'espère que ca vous donnera un coup de pouce supplémentaire pour ceux qui ne peuvent venir au labo :eyes: