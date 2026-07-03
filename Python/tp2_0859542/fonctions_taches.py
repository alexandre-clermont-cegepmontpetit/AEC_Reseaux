"""
Fichier : fonctions_taches.py

Objectif :
    Définir les fonctions utilisées par le gestionnaire de tâches.

Important :
    Ce fichier contient uniquement les fonctions.
    Le menu principal se trouve dans le fichier programme_principal.py.
    Les tests se trouvent dans le fichier tests_fonctions.py.
"""

import json
from pathlib import Path


def ajouter_tache(liste_taches, titre, priorite, categorie):
    """
    Ajoute une nouvelle tâche dans la liste.

    Retour :
        dict : la tâche créée.
    """

    # TODO
    # Créer un dictionnaire représentant la tâche.
    # Le dictionnaire doit contenir :
    #   - "titre"
    #   - "priorite"
    #   - "categorie"
    #   - "terminee" avec la valeur False
    tache = {
        "titre": titre,
        "priorite": priorite,
        "categorie": categorie,
        "terminee": False
    }

    # TODO
    # Ajouter la tâche dans la liste liste_taches.
    liste_taches.append(tache)

    # TODO
    # Retourner la tâche créée.
    return tache


def afficher_taches(liste_taches):
    """
    Affiche toutes les tâches de la liste.
    """

    # TODO
    # Vérifier si la liste est vide.
    # Si elle est vide, afficher un message.
    if len(liste_taches) == 0:
        print("Aucune tâche à afficher.")
    else:
        # TODO
        # Sinon, parcourir la liste avec une boucle for.
        numero = 1

        # TODO
        # Pour chaque tâche :
        #   - déterminer son état : "Terminée" ou "À faire"
        #   - afficher le titre
        #   - afficher la catégorie
        #   - afficher la priorité
        #   - afficher l'état
        for tache in liste_taches:
            # Déterminer l'état de la tâche.
            if tache["terminee"]:
                etat = "Terminée"
            else:
                etat = "À faire"

            # Afficher le titre, la catégorie, la priorité et l'état.
            print(f"{numero}. {tache['titre']} | "
                  f"Catégorie : {tache['categorie']} | "
                  f"Priorité : {tache['priorite']} | "
                  f"État : {etat}")

            numero += 1


def rechercher_tache(liste_taches, titre):
    """
    Recherche une tâche à partir de son titre.

    Retour :
        dict : la tâche trouvée.
        None : si aucune tâche n'est trouvée.
    """

    # TODO
    # Parcourir la liste des tâches.
    for tache in liste_taches:
        # TODO
        # Comparer le titre de chaque tâche avec le titre recherché.
        # La comparaison peut être faite sans tenir compte des majuscules/minuscules.
        if tache["titre"].lower() == titre.lower():
            # TODO
            # Si la tâche est trouvée, retourner cette tâche.
            return tache

    # TODO
    # Si aucune tâche n'est trouvée, retourner None.
    return None


def terminer_tache(liste_taches, titre):
    """
    Marque une tâche comme terminée.

    Retour :
        bool : True si la tâche a été trouvée et modifiée.
               False sinon.
    """

    # TODO
    # Rechercher la tâche à l'aide de la fonction rechercher_tache().
    tache = rechercher_tache(liste_taches, titre)

    # TODO
    # Si la tâche existe :
    #   - modifier la valeur de "terminee" à True
    #   - retourner True
    if tache is not None:
        tache["terminee"] = True
        return True

    # TODO
    # Sinon, retourner False.
    return False


def statistiques(liste_taches):
    """
    Affiche les statistiques des tâches.
    """

    # TODO
    # Calculer le nombre total de tâches.
    total = len(liste_taches)

    # TODO
    # Calculer le nombre de tâches terminées.
    terminees = 0

    for tache in liste_taches:
        if tache["terminee"]:
            terminees += 1

    # TODO
    # Calculer le nombre de tâches non terminées.
    non_terminees = total - terminees

    # TODO
    # Afficher les statistiques.
    print(f"Nombre total de tâches : {total}")
    print(f"Tâches terminées : {terminees}")
    print(f"Tâches non terminées : {non_terminees}")


def filtrer_par_categorie(liste_taches, categorie):
    """
    Filtre les tâches selon une catégorie.

    Retour :
        list : liste des tâches correspondant à la catégorie.
    """

    # TODO
    # Créer une liste vide pour stocker les tâches filtrées.
    taches_filtrees = []

    # TODO
    # Parcourir les tâches avec une boucle for.
    for tache in liste_taches:
        # TODO
        # Si la catégorie de la tâche correspond à la catégorie recherchée,
        # ajouter cette tâche dans la liste résultat.
        if tache["categorie"] == categorie:
            taches_filtrees.append(tache)

    # TODO
    # Retourner la liste résultat.
    return taches_filtrees


def sauvegarder_taches(liste_taches, nom_fichier):
    """
    Sauvegarde toutes les tâches dans un fichier JSON.
    """

    # TODO
    # Ouvrir le fichier en mode écriture.
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        # TODO
        # Utiliser json.dump() pour sauvegarder la liste dans le fichier.
        # Utiliser :
        #   - indent=4
        #   - ensure_ascii=False
        json.dump(liste_taches, fichier, indent=4, ensure_ascii=False)


def charger_taches(nom_fichier):
    """
    Charge les tâches à partir d'un fichier JSON.

    Retour :
        list : liste des tâches chargées.
               liste vide si le fichier n'existe pas.
    """

    # TODO
    # Créer un objet Path à partir du nom du fichier.
    chemin = Path(nom_fichier)

    # TODO
    # Vérifier si le fichier existe.
    if chemin.exists():
        # TODO
        # Si le fichier existe :
        #   - ouvrir le fichier en mode lecture
        #   - charger son contenu avec json.load()
        #   - retourner la liste chargée
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)

    # TODO
    # Si le fichier n'existe pas, retourner une liste vide.
    return []


def sauvegarder_par_categorie(liste_taches):
    """
    Sauvegarde les tâches dans plusieurs fichiers JSON,
    un fichier par catégorie.
    """

    # TODO
    # Créer un dictionnaire vide pour regrouper les tâches.
    #
    # Exemple :
    # {
    #     "Cours": [tache1, tache2],
    #     "Personnel": [tache3]
    # }
    categories = {}

    # TODO
    # Parcourir la liste des tâches.
    for tache in liste_taches:
        # TODO
        # Pour chaque tâche :
        #   - récupérer sa catégorie
        #   - vérifier si cette catégorie existe déjà dans le dictionnaire
        #   - sinon, créer une nouvelle entrée
        #   - ajouter la tâche dans la bonne catégorie
        categorie = tache["categorie"]

        if categorie not in categories:
            categories[categorie] = []

        categories[categorie].append(tache)

    # TODO
    # Parcourir le dictionnaire des catégories.
    for categorie in categories:
        # TODO
        # Pour chaque catégorie :
        #   - créer un nom de fichier sous la forme categorie.json
        #   - sauvegarder la liste des tâches de cette catégorie dans ce fichier
        nom_fichier = categorie + ".json"

        sauvegarder_taches(categories[categorie], nom_fichier)