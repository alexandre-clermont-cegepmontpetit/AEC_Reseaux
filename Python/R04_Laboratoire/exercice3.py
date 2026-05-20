# Exercice 3 — Liste d'utilisateurs

# Création de la liste de dictionnaires
utilisateurs = [
    {"nom": "Dupont", "prenom": "Alice", "age": 28, "admin": True},
    {"nom": "Martin", "prenom": "Bob", "age": 35, "admin": False},
    {"nom": "Durand", "prenom": "Claire", "age": 42, "admin": True},
    {"nom": "Petit", "prenom": "David", "age": 22, "admin": False}
]

# Afficher tous les utilisateurs
print("Tous les utilisateurs :")
for u in utilisateurs:
    print(u)

# Afficher seulement les utilisateurs admins
print("\nUtilisateurs administrateurs :")
for u in utilisateurs:
    if u["admin"]:
        print(u["prenom"], u["nom"])

# Compter les utilisateurs dont l'âge est plus grand que 36
nb = 0
for u in utilisateurs:
    if u["age"] > 36:
        nb += 1
print("\nNombre d'utilisateurs de plus de 36 ans :", nb)
