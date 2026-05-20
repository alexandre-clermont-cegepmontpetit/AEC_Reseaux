# Exercice 8 — Jeu de score

nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))

if nombre1 == nombre2 and nombre2 == nombre3:
    # Les 3 nombres sont égaux
    score = 100
elif nombre1 == nombre2 or nombre1 == nombre3 or nombre2 == nombre3:
    # Au moins 2 nombres sont égaux
    score = 75
else:
    # Aucun nombre égal
    score = nombre1 + nombre2 + nombre3

print(f"Votre score est : {score} points")
