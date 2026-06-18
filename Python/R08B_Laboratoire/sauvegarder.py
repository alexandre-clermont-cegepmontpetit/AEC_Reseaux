# Exercice 1
# Sauvegarder une liste de nombres dans un fichier JSON
# Utilisation :
#     python3 sauvegarder.py
#     python3 sauvegarder.py 12 8 25 4 17

import json
import sys


def version_1():
    # Sauvegarde une liste de nombres definie directement dans le code.
    nombres = [12, 8, 25, 4, 17]

    # On ouvre le fichier en mode écriture ("w") puis on y écrit la liste.
    with open("nombres.json", "w") as fichier:
        json.dump(nombres, fichier)

    print("Liste sauvegardée dans nombres.json :", nombres)


def version_2(nombres):
    # Sauvegarde une liste de nombres reçue en paramètres.
    with open("nombres.json", "w") as fichier:
        json.dump(nombres, fichier)

    print("Liste sauvegardée dans nombres.json :", nombres)


# sys.argv contient les arguments de la ligne de commande.
# sys.argv[0] est le nom du programme, on l'ignore donc.
if len(sys.argv) > 1:
    # Il y a des arguments -> Version 2
    # On convertit chaque argument (du texte) en nombre entier.
    nombres = [int(valeur) for valeur in sys.argv[1:]]
    version_2(nombres)
else:
    # Aucun argument -> Version 1
    version_1()