"""
Fichier : fonctions_taches.py

Objectif :
    Définir les fonctions utilisées par le gestionnaire de tâches.

Important :
    Ce fichier contient uniquement les fonctions.
    Le menu principal se trouve dans le fichier tp2.py.
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

    # Créer un dictionnaire représentant la tâche.
    tache = {
        "titre": titre,
        "priorite": priorite,
        "categorie": categorie,
        "terminee": False
    }

    # Ajouter la tâche dans la liste liste_taches.
    liste_taches.append(tache)

    # Retourner la tâche créée.
    return tache


def afficher_taches(liste_taches):
    """
    Affiche toutes les tâches de la liste.
    """

    # Vérifier si la liste est vide.
    if len(liste_taches) == 0:
        print("Aucune tâche à afficher.")
    else:
        # Parcourir la liste avec une boucle for.
        numero = 1

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

    # Parcourir la liste des tâches.
    for tache in liste_taches:
        # Comparer les titres sans tenir compte des majuscules/minuscules.
        if tache["titre"].lower() == titre.lower():
            # La tâche est trouvée : la retourner.
            return tache

    # Aucune tâche n'a été trouvée.
    return None


def terminer_tache(liste_taches, titre):
    """
    Marque une tâche comme terminée.

    Retour :
        bool : True si la tâche a été trouvée et modifiée.
               False sinon.
    """

    # Rechercher la tâche à l'aide de la fonction rechercher_tache().
    tache = rechercher_tache(liste_taches, titre)

    # Si la tâche existe, la marquer comme terminée.
    if tache is not None:
        tache["terminee"] = True
        return True

    # La tâche n'a pas été trouvée.
    return False


def statistiques(liste_taches):
    """
    Affiche les statistiques des tâches.
    """

    # Calculer le nombre total de tâches.
    total = len(liste_taches)

    # Calculer le nombre de tâches terminées.
    terminees = 0

    for tache in liste_taches:
        if tache["terminee"]:
            terminees += 1

    # Calculer le nombre de tâches non terminées.
    non_terminees = total - terminees

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

    # Créer une liste vide pour stocker les tâches filtrées.
    taches_filtrees = []

    # Parcourir les tâches avec une boucle for.
    for tache in liste_taches:
        # Si la catégorie correspond, ajouter la tâche au résultat.
        if tache["categorie"] == categorie:
            taches_filtrees.append(tache)

    # Retourner la liste résultat.
    return taches_filtrees


def sauvegarder_taches(liste_taches, nom_fichier):
    """
    Sauvegarde toutes les tâches dans un fichier JSON.
    """

    # Ouvrir le fichier en mode écriture.
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        # Sauvegarder la liste dans le fichier avec json.dump().
        json.dump(liste_taches, fichier, indent=4, ensure_ascii=False)


def charger_taches(nom_fichier):
    """
    Charge les tâches à partir d'un fichier JSON.

    Retour :
        list : liste des tâches chargées.
               liste vide si le fichier n'existe pas.
    """

    # Créer un objet Path à partir du nom du fichier.
    chemin = Path(nom_fichier)

    # Vérifier si le fichier existe.
    if chemin.exists():
        # Ouvrir le fichier en mode lecture et charger son contenu.
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)

    # Le fichier n'existe pas : retourner une liste vide.
    return []


def sauvegarder_par_categorie(liste_taches):
    """
    Sauvegarde les tâches dans plusieurs fichiers JSON,
    un fichier par catégorie.
    """

    # Créer un dictionnaire vide pour regrouper les tâches.
    #
    # Exemple :
    # {
    #     "Cours": [tache1, tache2],
    #     "Personnel": [tache3]
    # }
    categories = {}

    # Parcourir la liste des tâches.
    for tache in liste_taches:
        # Récupérer la catégorie de la tâche.
        categorie = tache["categorie"]

        # Si la catégorie n'existe pas encore, créer une nouvelle entrée.
        if categorie not in categories:
            categories[categorie] = []

        # Ajouter la tâche dans la bonne catégorie.
        categories[categorie].append(tache)

    # Parcourir le dictionnaire des catégories.
    for categorie in categories:
        # Créer un nom de fichier sous la forme categorie.json
        nom_fichier = categorie + ".json"

        # Sauvegarder la liste des tâches de cette catégorie.
        sauvegarder_taches(categories[categorie], nom_fichier)
