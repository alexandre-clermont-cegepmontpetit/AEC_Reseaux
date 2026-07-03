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

    # TODO
    # Ajouter la tâche dans la liste liste_taches.

    # TODO
    # Retourner la tâche créée.

    pass


def afficher_taches(liste_taches):
    """
    Affiche toutes les tâches de la liste.
    """

    # TODO
    # Vérifier si la liste est vide.
    # Si elle est vide, afficher un message.

    # TODO
    # Sinon, parcourir la liste avec une boucle for.

    # TODO
    # Pour chaque tâche :
    #   - déterminer son état : "Terminée" ou "À faire"
    #   - afficher le titre
    #   - afficher la catégorie
    #   - afficher la priorité
    #   - afficher l'état

    pass


def rechercher_tache(liste_taches, titre):
    """
    Recherche une tâche à partir de son titre.

    Retour :
        dict : la tâche trouvée.
        None : si aucune tâche n'est trouvée.
    """

    # TODO
    # Parcourir la liste des tâches.

    # TODO
    # Comparer le titre de chaque tâche avec le titre recherché.
    # La comparaison peut être faite sans tenir compte des majuscules/minuscules.

    # TODO
    # Si la tâche est trouvée, retourner cette tâche.

    # TODO
    # Si aucune tâche n'est trouvée, retourner None.

    pass


def terminer_tache(liste_taches, titre):
    """
    Marque une tâche comme terminée.

    Retour :
        bool : True si la tâche a été trouvée et modifiée.
               False sinon.
    """

    # TODO
    # Rechercher la tâche à l'aide de la fonction rechercher_tache().

    # TODO
    # Si la tâche existe :
    #   - modifier la valeur de "terminee" à True
    #   - retourner True

    # TODO
    # Sinon, retourner False.

    pass


def statistiques(liste_taches):
    """
    Affiche les statistiques des tâches.
    """

    # TODO
    # Calculer le nombre total de tâches.

    # TODO
    # Calculer le nombre de tâches terminées.

    # TODO
    # Calculer le nombre de tâches non terminées.

    # TODO
    # Afficher les statistiques.

    pass


def filtrer_par_categorie(liste_taches, categorie):
    """
    Filtre les tâches selon une catégorie.

    Retour :
        list : liste des tâches correspondant à la catégorie.
    """

    # TODO
    # Créer une liste vide pour stocker les tâches filtrées.

    # TODO
    # Parcourir les tâches avec une boucle for.

    # TODO
    # Si la catégorie de la tâche correspond à la catégorie recherchée,
    # ajouter cette tâche dans la liste résultat.

    # TODO
    # Retourner la liste résultat.

    pass


def sauvegarder_taches(liste_taches, nom_fichier):
    """
    Sauvegarde toutes les tâches dans un fichier JSON.
    """

    # TODO
    # Ouvrir le fichier en mode écriture.

    # TODO
    # Utiliser json.dump() pour sauvegarder la liste dans le fichier.
    # Utiliser :
    #   - indent=4
    #   - ensure_ascii=False

    pass


def charger_taches(nom_fichier):
    """
    Charge les tâches à partir d'un fichier JSON.

    Retour :
        list : liste des tâches chargées.
               liste vide si le fichier n'existe pas.
    """

    # TODO
    # Créer un objet Path à partir du nom du fichier.

    # TODO
    # Vérifier si le fichier existe.

    # TODO
    # Si le fichier existe :
    #   - ouvrir le fichier en mode lecture
    #   - charger son contenu avec json.load()
    #   - retourner la liste chargée

    # TODO
    # Si le fichier n'existe pas, retourner une liste vide.

    pass


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

    # TODO
    # Parcourir la liste des tâches.

    # TODO
    # Pour chaque tâche :
    #   - récupérer sa catégorie
    #   - vérifier si cette catégorie existe déjà dans le dictionnaire
    #   - sinon, créer une nouvelle entrée
    #   - ajouter la tâche dans la bonne catégorie

    # TODO
    # Parcourir le dictionnaire des catégories.

    # TODO
    # Pour chaque catégorie :
    #   - créer un nom de fichier sous la forme categorie.json
    #   - sauvegarder la liste des tâches de cette catégorie dans ce fichier

    pass