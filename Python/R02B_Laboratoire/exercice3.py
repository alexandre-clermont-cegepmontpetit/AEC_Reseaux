# Exercice 3 — Équation du Second Degré (ax² + bx + c = 0)
# Calcule les solutions réelles d'une équation du second degré
# en utilisant le discriminant.

import math

# Saisie des coefficients
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

# Vérification que a n'est pas nul (sinon ce n'est pas du second degré)
if a == 0:
    print("Ce n'est pas une équation du second degré (a doit être différent de 0).")
else:
    # Calcul du discriminant : Delta = b² - 4ac
    delta = b**2 - 4 * a * c
    print(f"Discriminant (Delta) = {delta}")

    # Analyse des cas selon le signe du discriminant
    if delta > 0:
        # Deux solutions réelles distinctes
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Deux solutions réelles : x1 = {x1} et x2 = {x2}")
    elif delta == 0:
        # Une solution unique (racine double)
        x = -b / (2 * a)
        print(f"Solution unique : x = {x}")
    else:
        # Pas de solution réelle (discriminant négatif)
        print("Pas de solution réelle")

# Cas de test (2 solutions): 2, 1, -1
# Cas de test (1 solution): 1, 4, 4
# Cas de test (0 solution): 1, 1, 1
# Cas de test (pas équation du second degré - droite): 0, 1, 2
