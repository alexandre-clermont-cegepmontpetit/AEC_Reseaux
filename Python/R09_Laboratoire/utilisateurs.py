# Exercice 4 - Consommer une API REST : liste d'utilisateurs
# API : https://jsonplaceholder.typicode.com/users
# Utilisation :
#     python utilisateurs.py

import requests

URL = "https://jsonplaceholder.typicode.com/users"


def recuperer_utilisateurs():
    # Envoie une requête GET et renvoie la liste des utilisateurs (liste de dictionnaires).
    reponse = requests.get(URL)
    return reponse.json()


def main():
    utilisateurs = recuperer_utilisateurs()

    # Pour chaque utilisateur : nom, courriel, ville et nom de la compagnie.
    print("Liste des utilisateurs :\n")
    for user in utilisateurs:
        nom = user["name"]
        courriel = user["email"]
        ville = user["address"]["city"]        # 'city' est imbriqué dans 'address'
        compagnie = user["company"]["name"]    # 'name' est imbriqué dans 'company'

        print(nom)
        print(f"   Courriel  : {courriel}")
        print(f"   Ville     : {ville}")
        print(f"   Compagnie : {compagnie}")
        print()

    # Statistiques
    total = len(utilisateurs)

    # Nombre d'utilisateurs dont le nom contient la lettre 'a' (majuscule ou minuscule)
    avec_a = 0
    for user in utilisateurs:
        if "a" in user["name"].lower():
            avec_a += 1

    print(f"Nombre total d'utilisateurs           : {total}")
    print(f"Utilisateurs dont le nom contient 'a' : {avec_a}")

    # Utilisateurs habitant à South Christy
    print("\nUtilisateur(s) habitant à South Christy :\n")
    for user in utilisateurs:
        if user["address"]["city"] == "South Christy":
            print(" -", user["name"])


main()
