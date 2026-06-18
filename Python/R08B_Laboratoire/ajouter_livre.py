# Exercice 6
# Ajouter un livre dans un fichier JSON contenant une liste de dictionnaires
# Utilisation :
#     python3 ajouter_livre.py
#     python3 ajouter_livre.py livres.json "Le Seigneur des anneaux" "J. R. R. Tolkien" 1954

import json
import sys


def ajouter_livre(nom_fichier, titre, auteur, annee):
    # Ajoute un nouveau livre a la liste contenue dans un fichier JSON.
    # Si le fichier n'existe pas encore, on part d'une liste vide.
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            livres = json.load(fichier)
    except FileNotFoundError:
        livres = []

    # Construire le dictionnaire qui représente le nouveau livre.
    nouveau_livre = {
        "titre": titre,
        "auteur": auteur,
        "annee": annee
    }

    # Ajouter ce livre à la fin de la liste.
    livres.append(nouveau_livre)

    # Réécrire la liste complète dans le fichier.
    # ensure_ascii=False : conserve les accents.  indent=4 : mise en forme lisible.
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(livres, fichier, ensure_ascii=False, indent=4)

    print("Livre ajouté :", nouveau_livre)
    print("Le fichier", nom_fichier, "contient maintenant", len(livres), "livre(s).")


# Pour la Version 2, on a besoin de 4 arguments : fichier, titre, auteur et année.
if len(sys.argv) > 4:
    nom_fichier = sys.argv[1]
    titre = sys.argv[2]
    auteur = sys.argv[3]
    annee = int(sys.argv[4])   # l'année arrive en texte -> on la convertit en entier
else:
    # Version 1 : informations définies directement dans le code.
    nom_fichier = "livres.json"
    titre = "1984"
    auteur = "George Orwell"
    annee = 1949

ajouter_livre(nom_fichier, titre, auteur, annee)