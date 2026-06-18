# Exercice 3
# Ajouter un nombre dans un fichier JSON
# Utilisation :
#     python3 ajouter.py
#     python3 ajouter.py nombres.json 30

import json
import sys


def ajouter_nombre(nom_fichier, nombre):
    # Ajoute un nouveau nombre a la liste contenue dans un fichier JSON.
    # 1. Lire la liste déjà présente dans le fichier.
    with open(nom_fichier, "r") as fichier:
        nombres = json.load(fichier)

    # 2. Ajouter le nouveau nombre à la fin de la liste.
    nombres.append(nombre)

    # 3. Réécrire la liste complète dans le fichier.
    with open(nom_fichier, "w") as fichier:
        json.dump(nombres, fichier)

    print("Nombre", nombre, "ajouté. Liste mise à jour :", nombres)


# On a besoin de 2 arguments : le fichier ET le nombre.
if len(sys.argv) > 2:
    # Version 2 : python3 ajouter.py nombres.json 30
    nom_fichier = sys.argv[1]
    nombre = int(sys.argv[2])
else:
    # Version 1 : valeurs définies dans le code.
    nom_fichier = "nombres.json"
    nombre = 30

ajouter_nombre(nom_fichier, nombre)