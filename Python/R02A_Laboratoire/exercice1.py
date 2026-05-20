# Exercice 1 — Pair ou impair
# Demande un nombre et affiche s'il est pair ou impair
 
nombre = int(input("Entrez un nombre : "))
 
if nombre % 2 == 0:
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")
