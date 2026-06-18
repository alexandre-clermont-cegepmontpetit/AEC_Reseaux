"""
Exercice 6 - Ajouter un livre dans un fichier JSON contenant une liste de dictionnaires

Le fichier JSON contient une LISTE de livres. Chaque livre est un dictionnaire
avec les cles : titre, auteur, annee.

Version 1 : les informations du livre sont definies directement dans le code.
Version 2 : les informations du livre sont fournies en parametres.

Utilisation :
    python3 exercice6.py
        -> Version 1 (livre defini dans le code)

    python3 exercice6.py livres.json "Le Seigneur des anneaux" "J. R. R. Tolkien" 1954
        -> Version 2 (fichier + titre + auteur + annee en parametres)
"""

import json
import sys


def ajouter_livre(nom_fichier, titre, auteur, annee):
    """Ajoute un nouveau livre a la liste contenue dans un fichier JSON."""
    # 1. Lire la liste de livres deja presente dans le fichier.
    #    Si le fichier n'existe pas encore, on part d'une liste vide.
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            livres = json.load(fichier)
    except FileNotFoundError:
        livres = []

    # 2. Construire le dictionnaire qui represente le nouveau livre.
    nouveau_livre = {
        "titre": titre,
        "auteur": auteur,
        "annee": annee
    }

    # 3. Ajouter ce livre a la fin de la liste.
    livres.append(nouveau_livre)

    # 4. Reecrire la liste complete dans le fichier.
    #    ensure_ascii=False : conserve les accents.  indent=4 : mise en forme lisible.
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(livres, fichier, ensure_ascii=False, indent=4)

    print("Livre ajoute :", nouveau_livre)
    print("Le fichier", nom_fichier, "contient maintenant", len(livres), "livre(s).")


if __name__ == "__main__":
    # Pour la Version 2, on a besoin de 4 arguments :
    # le fichier, le titre, l'auteur et l'annee.
    if len(sys.argv) > 4:
        nom_fichier = sys.argv[1]
        titre = sys.argv[2]
        auteur = sys.argv[3]
        annee = int(sys.argv[4])   # l'annee arrive en texte -> on la convertit en entier
    else:
        # Version 1 : informations definies directement dans le code.
        nom_fichier = "livres.json"
        titre = "1984"
        auteur = "George Orwell"
        annee = 1949

    ajouter_livre(nom_fichier, titre, auteur, annee)
