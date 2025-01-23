function trierParNom() {
    // Récupérer le tableau HTML
    const tableau = document.getElementById('table');

    // Extraire toutes les lignes (rows) du corps du tableau
    const lignesTableau = Array.from(tableau.tBodies[0].rows);

    // Trier les lignes en fonction du contenu de la première colonne (Nom)
    lignesTableau.sort((ligneA, ligneB) => {
        // Extraire et nettoyer le texte de la première cellule (colonne Nom) pour chaque ligne
        const nomLigneA = ligneA.cells[0].textContent.trim().toLowerCase();
        const nomLigneB = ligneB.cells[0].textContent.trim().toLowerCase();

        // Comparer les noms en respectant l'ordre alphabétique
        return nomLigneA.localeCompare(nomLigneB);
    });

    // Réinsérer les lignes triées dans le tableau
    lignesTableau.forEach(ligneTriee => tableau.tBodies[0].appendChild(ligneTriee));
}