# Exercice 1 - Consommer une API REST : une publication
# API : https://jsonplaceholder.typicode.com/posts/<id>
# Utilisation :
#     python publication.py          # affiche la publication n 1 (par défaut)
#     python publication.py 5        # affiche la publication n 5

import sys
import requests


def recuperer_publication(post_id):
    # Envoie une requête GET et renvoie les données JSON de la publication.
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    reponse = requests.get(url)
    return reponse.json()             # convertit la réponse JSON en dictionnaire Python


def main():
    # L'identifiant est lu depuis la ligne de commande.
    # S'il n'est pas fourni, on utilise 1 par défaut.
    if len(sys.argv) > 1:
        post_id = sys.argv[1]
    else:
        post_id = 1

    publication = recuperer_publication(post_id)

    # Affichage des informations demandées
    print("Identifiant :", publication["id"])
    print("Titre       :", publication["title"])
    print("Contenu     :", publication["body"])


main()