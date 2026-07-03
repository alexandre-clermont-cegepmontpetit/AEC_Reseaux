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

    # Vérifier que l'utilisateur a fourni le nom du
    # fichier JSON lors de l'exécution du programme.
    if len(sys.argv) != 2:
        print("Erreur : vous devez fournir le nom du fichier JSON.")
        print("Exemple : python3 tp2.py taches.json")
        sys.exit(1)

    # =====================================================
    # Charger les tâches
    # =====================================================

    # Récupérer le nom du fichier JSON.
    nom_fichier = sys.argv[1]

    # Vérifier que le fichier existe.
    if not os.path.exists(nom_fichier):
        print(f"Erreur : le fichier {nom_fichier} n'existe pas.")
        sys.exit(1)

    # Charger les tâches à l'aide de la fonction charger_taches().
    liste_taches = charger_taches(nom_fichier)

    # =====================================================
    # Initialiser la variable de contrôle du menu
    # =====================================================

    choix = ""

    # =====================================================
    # Boucle principale
    # =====================================================

    while choix != "9":

        # Afficher le menu.
        afficher_menu()

        # Demander le choix de l'utilisateur.
        choix = input("Votre choix : ")

        # =================================================
        # Option 1 : Ajouter une tâche
        # =================================================

        if choix == "1":

            # Demander le titre, la priorité et la catégorie.
            titre = input("Titre de la tâche : ")
            priorite = int(input("Priorité (1 à 3) : "))
            categorie = input("Catégorie : ")

            # Appeler la fonction ajouter_tache().
            ajouter_tache(liste_taches, titre, priorite, categorie)

            print("Tâche ajoutée.")

        # =================================================
        # Option 2 : Afficher les tâches
        # =================================================

        elif choix == "2":

            # Appeler la fonction afficher_taches().
            afficher_taches(liste_taches)

        # =================================================
        # Option 3 : Rechercher une tâche
        # =================================================

        elif choix == "3":

            # Demander le titre à rechercher.
            titre = input("Titre à rechercher : ")

            # Appeler la fonction rechercher_tache().
            tache = rechercher_tache(liste_taches, titre)

            # Afficher la tâche trouvée ou un message d'erreur.
            if tache is not None:
                print(f"Tâche trouvée : {tache}")
            else:
                print("Tâche introuvable.")

        # =================================================
        # Option 4 : Terminer une tâche
        # =================================================

        elif choix == "4":

            # Demander le titre de la tâche.
            titre = input("Titre de la tâche à terminer : ")

            # Appeler la fonction terminer_tache() et afficher
            # un message indiquant si la tâche a été trouvée.
            if terminer_tache(liste_taches, titre):
                print("La tâche est maintenant terminée.")
            else:
                print("Tâche introuvable.")

        # =================================================
        # Option 5 : Afficher les statistiques
        # =================================================

        elif choix == "5":

            # Appeler la fonction statistiques().
            statistiques(liste_taches)

        # =================================================
        # Option 6 : Filtrer par catégorie
        # =================================================

        elif choix == "6":

            # Demander une catégorie.
            categorie = input("Catégorie recherchée : ")

            # Appeler filtrer_par_categorie().
            taches_filtrees = filtrer_par_categorie(liste_taches, categorie)

            # Afficher les tâches obtenues.
            afficher_taches(taches_filtrees)

        # =================================================
        # Option 7 : Sauvegarder
        # =================================================

        elif choix == "7":

            # Sauvegarder les tâches dans le fichier JSON.
            sauvegarder_taches(liste_taches, nom_fichier)

            print("Tâches sauvegardées.")

        # =================================================
        # Option 8 : Sauvegarder par catégorie
        # =================================================

        elif choix == "8":

            # Sauvegarder les tâches dans un fichier JSON
            # distinct pour chaque catégorie.
            sauvegarder_par_categorie(liste_taches)

            print("Tâches sauvegardées par catégorie.")

        # =================================================
        # Option 9 : Quitter
        # =================================================

        elif choix == "9":

            # Sauvegarder les tâches avant de quitter.
            sauvegarder_taches(liste_taches, nom_fichier)

            # Afficher un message de fermeture.
            print("Tâches sauvegardées. Au revoir!")

        else:

            print("Choix invalide.")


# Point d'entrée du programme

programme_principal()
