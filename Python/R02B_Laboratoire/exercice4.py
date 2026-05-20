# Exercice 4 — Année bissextile
# Vérifie si une année donnée est bissextile.
#
# Une année est bissextile si :
#   - Elle est divisible par 400
#   OU
#   - Elle est divisible par 4 mais pas par 100

# Saisie de l'année
annee = int(input("Entrez une année : "))

# Vérification de la condition de bissextilité
if (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0):
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")

# Cas de test (pas bissextile): 2026
# Cas de test (bissextile): 2028