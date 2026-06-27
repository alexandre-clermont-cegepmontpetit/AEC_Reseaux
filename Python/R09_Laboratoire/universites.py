# Exercice 3 - Consommer une API REST : universités d'un pays
# API : http://universities.hipolabs.com/search?country=<pays>
# Utilisation :
#     python universites.py          # pays = Canada (par défaut)
#     python universites.py France   # pays = France

import sys
import requests


def recuperer_universites(pays):
    # Envoie une requête GET et renvoie la liste des universités (liste de dictionnaires).
    url = "http://universities.hipolabs.com/search"
    parametres = {"country": pays}            # construit ...?country=<pays>
    reponse = requests.get(url, params=parametres)
    return reponse.json()


def main():
    # Le pays est lu depuis la ligne de commande ; Canada par défaut.
    # On joint les arguments pour gérer aussi les pays en deux mots (ex. United States).
    if len(sys.argv) > 1:
        pays = " ".join(sys.argv[1:])
    else:
        pays = "Canada"

    universites = recuperer_universites(pays)

    # Nom des 10 premières universités
    print(f"Les 10 premières universités en {pays} :\n")
    for uni in universites[:10]:
        print(" -", uni["name"])

    # Nom + site web de chaque université
    print("\nNom et site web de chaque université :\n")
    for uni in universites:
        # web_pages est une liste ; on prend la première adresse si elle existe.
        site = uni["web_pages"][0] if uni["web_pages"] else "(aucun site)"
        print(f" - {uni['name']} : {site}")

    # Nombre total d'universités
    print(f"\nNombre total d'universités : {len(universites)}")


main()