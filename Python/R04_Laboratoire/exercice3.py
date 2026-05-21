# Exercice 3 — Liste d'utilisateurs

# Création de la liste de dictionnaires
utilisateurs = [
    {"nom": "Dupont", "prenom": "Alice", "age": 28, "admin": True},
    {"nom": "Martin", "prenom": "Bob", "age": 35, "admin": False},
    {"nom": "Durand", "prenom": "Claire", "age": 42, "admin": True},
    {"nom": "Petit", "prenom": "David", "age": 22, "admin": False}
]

# Afficher tous les utilisateurs
print("=== TOUS LES UTILISATEURS ===")
for u in utilisateurs:
    print(u)

# Afficher seulement les utilisateurs admins
print("\n=== UTILISATEURS ADMIN ===")
for u in utilisateurs:
    if u["admin"]:
        print(u)

# Compter les utilisateurs dont l'âge est plus grand que 36
print("\n=== UTILISATEURS AVEC ÂGE > 34 ===")
nb = 0
for u in utilisateurs:
    if u["age"] > 34:
        nb += 1
print("Nombre d'utilisateurs âgés de plus de 34 :", nb)
