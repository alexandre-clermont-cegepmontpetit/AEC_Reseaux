# Exercice 2
# Lire un fichier JSON contenant une liste de nombres
# Utilisation :
#     python3 lire.py
#     python3 lire.py nombres.json

import json
import sys


def lire_nombres(nom_fichier):
    # Lit un fichier JSON et affiche tous les nombres qu'il contient.
    with open(nom_fichier, "r") as fichier:
        nombres = json.load(fichier)

    print("Nombres contenus dans", nom_fichier, ":")
    for nombre in nombres:
        print(nombre)


if len(sys.argv) > 1:
    # Version 2 : le nom du fichier vient de la ligne de commande.
    nom_fichier = sys.argv[1]
else:
    # Version 1 : le nom du fichier est écrit dans le code.
    nom_fichier = "nombres.json"

lire_nombres(nom_fichier)
