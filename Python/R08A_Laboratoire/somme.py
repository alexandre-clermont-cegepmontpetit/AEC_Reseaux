# Exercice 2
# Reçoit deux nombres, calcule puis affiche la somme.
# Utilisation :
#     python3 somme.py 12 7
import sys

if len(sys.argv) != 3:
    print("Utilisation : python somme.py <nombre1> <nombre2>")
    sys.exit(1)

# Convertir les arguments en nombres avec int() avant de calculer.
a = int(sys.argv[1])
b = int(sys.argv[2])

print(f"La somme est : {a + b}")
