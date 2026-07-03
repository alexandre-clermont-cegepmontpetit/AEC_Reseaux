import sys
import os
from fonctions_taches import *





def afficher_menu():
    """
    Affiche le menu principal de l'application.
    """
    print("\n===== Gestionnaire de tâches =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("4. Terminer une tâche")
    print("5. Afficher les statistiques")
    print("6. Filtrer par catégorie")
    print("7. Sauvegarder")
    print("8. Sauvegarder par catégorie")
    print("9. Quitter")
   


def programme_principal():
    """
    Fonction principale du programme.

    Cette fonction doit :

    1. Vérifier les paramètres de ligne de commande.
    2. Charger les tâches à partir du fichier JSON.
    3. Afficher le menu dans une boucle.
    4. Exécuter le traitement correspondant au choix de l'utilisateur.
    5. Sauvegarder les données avant de quitter.
    """

    # =====================================================
    # Vérifier les paramètres de ligne de commande
    # =====================================================

    # TODO
    # Vérifier que l'utilisateur a fourni le nom du
    # fichier JSON lors de l'exécution du programme.
    #
    # Exemple :
    #
    # python3 tp2.py taches.json
    #
    # Si aucun fichier n'est fourni :
    #   - afficher un message d'erreur
    #   - terminer le programme

    # =====================================================
    # Charger les tâches
    # =====================================================

    # TODO
    # Récupérer le nom du fichier JSON.

    # Vérifier que le fichier existe.
    # Si le fichier n'existe pas :
    #   - afficher un message d'erreur
    #   - terminer le programme

    # TODO
    # Charger les tâches à l'aide de la fonction
    # charger_taches().

    # =====================================================
    # Initialiser la variable de contrôle du menu
    # =====================================================

    # TODO
    # Créer une variable permettant de conserver
    # le choix de l'utilisateur.

    choix = ""

    # =====================================================
    # Boucle principale
    # =====================================================

    while choix != "9":

        # TODO
        # Afficher le menu.

        # TODO
        # Demander le choix de l'utilisateur.

        # =================================================
        # Option 1 : Ajouter une tâche
        # =================================================

        if choix == "1":

            # TODO
            # Demander :
            #   - le titre
            #   - la priorité
            #   - la catégorie

            # TODO
            # Appeler la fonction ajouter_tache()

            pass

        # =================================================
        # Option 2 : Afficher les tâches
        # =================================================

        elif choix == "2":

            # TODO
            # Appeler la fonction afficher_taches()

            pass

        # =================================================
        # Option 3 : Rechercher une tâche
        # =================================================

        elif choix == "3":

            # TODO
            # Demander le titre à rechercher.

            # TODO
            # Appeler la fonction rechercher_tache().

            # TODO
            # Afficher la tâche trouvée ou un message
            # indiquant qu'elle est introuvable.

            pass

        # =================================================
        # Option 4 : Terminer une tâche
        # =================================================

        elif choix == "4":

            # TODO
            # Demander le titre de la tâche.

            # TODO
            # Appeler la fonction terminer_tache().

            # TODO
            # Afficher un message indiquant si la tâche
            # a été trouvée ou non.

            pass

        # =================================================
        # Option 5 : Afficher les statistiques
        # =================================================

        elif choix == "5":

            # TODO
            # Appeler la fonction statistiques()

            pass

        # =================================================
        # Option 6 : Filtrer par catégorie
        # =================================================

        elif choix == "6":

            # TODO
            # Demander une catégorie.

            # TODO
            # Appeler filtrer_par_categorie().

            # TODO
            # Afficher les tâches obtenues.

            pass

        # =================================================
        # Option 7 : Sauvegarder
        # =================================================

        elif choix == "7":

            # TODO
            # Sauvegarder les tâches dans le fichier JSON.

            pass

        # =================================================
        # Option 8 : Sauvegarder par catégorie
        # =================================================

        elif choix == "8":

            # TODO
            # Sauvegarder les tâches dans un fichier JSON
            # distinct pour chaque catégorie.

            pass

        # =================================================
        # Option 9 : Quitter
        # =================================================

        elif choix == "9":

            # TODO
            # Sauvegarder les tâches avant de quitter.

            # TODO
            # Afficher un message de fermeture.

            pass

        else:

            print("Choix invalide.")


# Point d'entrée du programme

programme_principal()