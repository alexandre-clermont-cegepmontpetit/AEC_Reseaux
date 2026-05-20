# Exercice 3 — Trouver le minimum entre 3 nombres

nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

# On suppose au départ que nombre1 est le plus petit
minimum = nombre1

if nombre2 < minimum:
    minimum = nombre2

if nombre3 < minimum:
    minimum = nombre3

print(f"Le plus petit est : {minimum}")
