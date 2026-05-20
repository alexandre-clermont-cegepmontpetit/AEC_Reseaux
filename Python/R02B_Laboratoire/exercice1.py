# Exercice 1 — Le Triangle Valide
# Vérifie si trois longueurs forment un triangle constructible
# et détermine son type (équilatéral, isocèle ou scalène).

# Saisie des trois côtés
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérification : un triangle est constructible si la somme de deux côtés
# est strictement supérieure au troisième côté (pour toutes les combinaisons)
if a + b > c and a + c > b and b + c > a:
    # Le triangle est valide, on détermine son type
    if a == b == c:
        type_triangle = "équilatéral"
    elif a == b or b == c or a == c:
        type_triangle = "isocèle"
    else:
        type_triangle = "scalène"

    print(f"Le triangle est valide et il est {type_triangle}.")
else:
    print("Le triangle n'est pas constructible avec ces côtés.")

# Cas de test (scalène): 3, 4, 5
# Cas de test (équilatéral): 6, 6, 6
# Cas de test (isocèle): 5, 5, 8
# Cas de test (triangle pas constructible avec ces côtés): 2, 3, 6