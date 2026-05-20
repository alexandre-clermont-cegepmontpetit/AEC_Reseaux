# Automatise la création de profils d'employés sur un serveur Linux

# Saisie des informations de l'employé
prenom = input("Prénom : ")
nom = input("Nom : ")
departement = input("Département : ")

# Construction du nom d'utilisateur : première lettre du prénom + nom (en minuscules)
nom_utilisateur = (prenom[0] + nom).lower()

# Affichage
print("--- Profil Créé ---")
print("Identifiant : " + nom_utilisateur)
print("Accès au groupe : " + departement)