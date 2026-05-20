# Exercice 7 — Multiple de 3 et 5

nombre = int(input("Entrez un nombre : "))

if nombre % 3 == 0 and nombre % 5 == 0:
    print(f"{nombre} est multiple de 3 et 5")
elif nombre % 3 == 0:
    print(f"{nombre} est multiple de 3 seulement")
elif nombre % 5 == 0:
    print(f"{nombre} est multiple de 5 seulement")
else:
    print(f"{nombre} n'est pas multiple de 3 et 5")
