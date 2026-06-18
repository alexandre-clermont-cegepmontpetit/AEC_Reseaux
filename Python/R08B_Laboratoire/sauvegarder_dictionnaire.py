# Exercice 4
# Sauvegarder un dictionnaire dans un fichier JSON
# Utilisation :
#     python3 sauvegarder_dictionnaire.py

import json


def sauvegarder_livre():
    # Sauvegarde un dictionnaire représentant un livre dans un fichier JSON.
    livre = {
        "titre": "Le Petit Prince",
        "auteur": "Antoine de Saint-Exupéry",
        "annee": 1943
    }

    # ensure_ascii=False : conserve les accents dans le fichier.
    # indent=4 : rend le fichier JSON plus lisible (mise en forme).
    with open("livre.json", "w", encoding="utf-8") as fichier:
        json.dump(livre, fichier, ensure_ascii=False, indent=4)

    print("Livre sauvegardé dans livre.json :")
    print(livre)


sauvegarder_livre()
