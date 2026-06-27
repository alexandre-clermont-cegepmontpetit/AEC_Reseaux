# Exercice 2 - Consommer une API REST : liste de tâches
# API : https://jsonplaceholder.typicode.com/todos
# Utilisation :
#     python taches.py               # affiche les 10 premières tâches + statistiques
#     python taches.py 1 5 20        # affiche uniquement les tâches 1, 5 et 20

import sys
import requests

URL = "https://jsonplaceholder.typicode.com/todos"


def recuperer_taches():
    # Envoie une requête GET et renvoie la liste des tâches (liste de dictionnaires).
    reponse = requests.get(URL)
    return reponse.json()


def afficher_tache(tache):
    # Affiche une tâche sur une ligne : identifiant, état et titre.
    etat = "terminee" if tache["completed"] else "non terminee"
    print(f"{tache['id']:>3} | {etat:<12} | {tache['title']}")


def main():
    taches = recuperer_taches()

    # Si des identifiants sont passés en paramètre, on n'affiche que ceux-là.
    ids_demandes = [int(arg) for arg in sys.argv[1:]]

    if ids_demandes:
        print(f"Tâches demandées : {ids_demandes}\n")
        a_afficher = [t for t in taches if t["id"] in ids_demandes]
    else:
        print("Les 10 premières tâches :\n")
        a_afficher = taches[:10]

    for tache in a_afficher:
        afficher_tache(tache)

    # Statistiques calculées sur l'ensemble des tâches
    terminees = 0
    non_terminees = 0
    for tache in taches:
        if tache["completed"]:
            terminees += 1
        else:
            non_terminees += 1

    total = len(taches)
    pourcentage = terminees / total * 100

    print()
    print(f"Nombre total de tâches          : {total}")
    print(f"Tâches terminées                : {terminees}")
    print(f"Tâches non terminées            : {non_terminees}")
    print(f"Pourcentage de tâches terminées : {pourcentage:.1f} %")


main()