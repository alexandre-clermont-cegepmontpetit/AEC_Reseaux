"""
TP1 - Mini système bancaire en Python
=====================================
Ce programme simule un petit systeme bancaire permettant à plusieurs
utilisateurs de se connecter, de consulter leur solde, de déposer ou
retirer de l'argent, de consulter leur historique et leurs statistiques.
"""

from datetime import datetime


# ---------------------------------------------------------------------------
# DONNÉES : liste de comptes (étape 5 - plusieurs comptes)
# Chaque compte est un dictionnaire. Tous les comptes sont dans une liste.
# ---------------------------------------------------------------------------
comptes = [
    {
        "login": "alice",
        "motdepasse": "1234",
        "nom": "Alice",
        "solde": 2450,
        "historique": [
            {
                "type": "depot",
                "montant": 1200,
                "date": "2026-05-01 09:15:00"
            },
            {
                "type": "retrait",
                "montant": 200,
                "date": "2026-05-02 14:20:00"
            }
        ]
    },
    {
        "login": "bob",
        "motdepasse": "abcd",
        "nom": "Bob",
        "solde": 800,
        "historique": []
    }
]


# ---------------------------------------------------------------------------
# FONCTIONS UTILITAIRES
# ---------------------------------------------------------------------------
def obtenir_date_formatee():
    """Retourne la date et l'heure actuelles sous forme de texte lisible."""
    maintenant = datetime.now()
    return maintenant.strftime("%Y-%m-%d %H:%M:%S")


def lire_montant(message):
    """
    Demande un montant à l'utilisateur et le valide.
    Retourne le montant (float) s'il est valide, sinon None.
    Gère les erreurs avec try/except :
        - texte au lieu d'un nombre  -> "Entrée invalide"
        - montant negatif ou nul     -> "Montant invalide"
    """
    try:
        montant = float(input(message))
    except ValueError:
        # L'utilisateur a entré du texte qui ne peut pas devenir un nombre
        print("Entree invalide")
        return None

    if montant <= 0:
        print("Montant invalide")
        return None

    return montant


# ---------------------------------------------------------------------------
# FONCTIONS DU MENU PRINCIPAL
# ---------------------------------------------------------------------------
def afficher_menu():
    """Affiche le menu principal du système bancaire."""
    print("\n===== MENU =====")
    print("1. Consulter le solde")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Afficher l'historique")
    print("5. Afficher statistiques")
    print("6. Déconnexion")


def consulter_solde(compte):
    """Affiche le solde actuel du compte connecté."""
    print("Votre solde est de :", compte["solde"], "$")


def deposer(compte):
    """
    Demande un montant, le valide, l'ajoute au solde
    et enregistre la transaction dans l'historique.
    """
    montant = lire_montant("Montant a déposer : ")
    if montant is None:
        return  # Le montant était invalide, on arrête ici

    # Mise a jour du solde
    compte["solde"] = compte["solde"] + montant

    # Enregistrement de la transaction
    transaction = {
        "type": "depot",
        "montant": montant,
        "date": obtenir_date_formatee()
    }
    compte["historique"].append(transaction)

    print("\nDépot effectué avec succès")
    print("Nouveau solde :", compte["solde"], "$")


def retirer(compte):
    """
    Demande un montant, le valide, vérifie les fonds disponibles,
    retire le montant du solde et enregistre la transaction.
    """
    montant = lire_montant("Montant a retirer : ")
    if montant is None:
        return  # Le montant était invalide, on arrête ici

    # Vérification des fonds suffisants
    if montant > compte["solde"]:
        print("Fonds insuffisants")
        return

    # Mise a jour du solde
    compte["solde"] = compte["solde"] - montant

    # Enregistrement de la transaction
    transaction = {
        "type": "retrait",
        "montant": montant,
        "date": obtenir_date_formatee()
    }
    compte["historique"].append(transaction)

    print("\nRetrait effectué")
    print("Nouveau solde :", compte["solde"], "$")


def afficher_historique(compte):
    """Affiche toutes les transactions du compte connecté."""
    print("\n=== HISTORIQUE ===")

    # Gestion du cas où aucune transaction n'existe
    if len(compte["historique"]) == 0:
        print("Aucune transaction pour le moment")
        return

    # Parcours de la liste des transactions
    for transaction in compte["historique"]:
        print()
        print("Type :", transaction["type"])
        print("Montant :", transaction["montant"], "$")
        print("Date :", transaction["date"])


def afficher_statistiques(compte):
    """Calcule et affiche le total des dépôts et des retraits."""
    total_depots = 0
    total_retraits = 0

    # Parcours de la liste pour additionner par type de transaction
    for transaction in compte["historique"]:
        if transaction["type"] == "depot":
            total_depots = total_depots + transaction["montant"]
        elif transaction["type"] == "retrait":
            total_retraits = total_retraits + transaction["montant"]

    print("\n=== STATISTIQUES ===")
    print("Total des retraits :", total_retraits, "$")
    print("Total des dépôts :", total_depots, "$")


# ---------------------------------------------------------------------------
# CONNEXION
# ---------------------------------------------------------------------------
def se_connecter():
    """
    Demande le login et le mot de passe, puis recherche le compte
    correspondant dans la liste des comptes.
    Retourne le compte trouvé, ou None si les identifiants sont invalides.
    """
    print("\n=== SYSTÈME BANCAIRE ===")
    login = input("Login : ")
    motdepasse = input("Mot de passe : ")

    # Recherche du compte correspondant
    for compte in comptes:
        if compte["login"] == login and compte["motdepasse"] == motdepasse:
            print("\nBienvenue", compte["nom"])
            return compte

    # Aucun compte ne correspond
    print("Identifiants invalides")
    return None


# ---------------------------------------------------------------------------
# PROGRAMME PRINCIPAL
# ---------------------------------------------------------------------------
def main():
    """Point d'entrée du programme : gère la connexion et le menu."""
    programme_actif = True

    while programme_actif:
        # Étape de connexion (on reste ici tant que la connexion échoue)
        compte_connecte = se_connecter()
        if compte_connecte is None:
            continue  # Identifiants invalides : on redemande la connexion

        # Boucle du menu bancaire (jusqu'à la déconnexion)
        connecte = True
        while connecte:
            afficher_menu()
            choix = input("Choix : ")

            if choix == "1":
                consulter_solde(compte_connecte)
            elif choix == "2":
                deposer(compte_connecte)
            elif choix == "3":
                retirer(compte_connecte)
            elif choix == "4":
                afficher_historique(compte_connecte)
            elif choix == "5":
                afficher_statistiques(compte_connecte)
            elif choix == "6":
                print("\nDéconnexion réussie. Au revoir", compte_connecte["nom"])
                connecte = False  # On sort du menu, retour à la connexion
            else:
                # Validation des choix invalides
                print("Choix invalide")

        # Apres la déconnexion, on demande si l'utilisateur veut quitter
        reponse = input("\nVoulez-vous quitter le programme ? (o/n) : ")
        if reponse.lower() == "o":
            programme_actif = False
            print("Programme terminé. A bientôt !")


# Lancement du programme
main()