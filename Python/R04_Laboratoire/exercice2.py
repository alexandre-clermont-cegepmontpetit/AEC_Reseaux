# Exercice 2 — Dictionnaire utilisateur

# Création du dictionnaire utilisateur
utilisateur = {
    "nom": "Dupond",
    "prenom": "Benjamin",
    "age": 28,
    "admin": True
}

# Afficher l'utilisateur
print("Utilisateur :", utilisateur)

# Vérifier si l'utilisateur est admin
if utilisateur["admin"]:
    print(utilisateur["prenom"], utilisateur["nom"], "est administrateur.")
else:
    print(utilisateur["prenom"], utilisateur["nom"], "n'est pas administrateur.")
