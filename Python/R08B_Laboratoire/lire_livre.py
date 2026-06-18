# Exercice 5
# Lire un fichier JSON dans un dictionnaire
# Utilisation :
#     python3 lire_livre.py
#     python3 lire_livre.py livre.json

import json
import sys


def lire_livre(nom_fichier):
    # Lit un fichier JSON contenant un livre et affiche ses informations.
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        livre = json.load(fichier)

    # On parcourt le dictionnaire pour afficher chaque clé et sa valeur.
    print("Informations du livre :")
    for cle, valeur in livre.items():
        print(cle, ":", valeur)


if len(sys.argv) > 1:
    # Version 2 : le nom du fichier vient de la ligne de commande.
    nom_fichier = sys.argv[1]
else:
    # Version 1 : le nom du fichier est écrit dans le code.
    nom_fichier = "livre.json"

lire_livre(nom_fichier)