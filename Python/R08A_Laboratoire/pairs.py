# Exercice 5
# Reçoit plusieurs nombres entiers et affiche uniquement les nombres pairs.
# Utilisation :
#     python3 pairs.py 12 7 5 18 21 30
import sys

if len(sys.argv) < 2:
    print("Utilisation : python pairs.py <nombre1> <nombre2> ...")
    sys.exit(1)

nombres = [int(x) for x in sys.argv[1:]]

# Un nombre est pair si le reste de sa division par 2 (l'opérateur %) vaut 0.
pairs = [n for n in nombres if n % 2 == 0]

print("Nombres pairs :", pairs)