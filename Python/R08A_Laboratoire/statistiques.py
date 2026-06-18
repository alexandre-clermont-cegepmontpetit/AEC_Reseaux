# Exercice 3
# Reçoit une série de nombres et affiche le nombre de valeurs,
# la somme, le minimum, le maximum et les valeurs triées par ordre croissant.
# Utilisation :
#     python3 statistiques.py 12 7 5 18 21 30
import sys

if len(sys.argv) < 2:
    print("Utilisation : python statistiques.py <nombre1> <nombre2> ...")
    sys.exit(1)

# On récupère tous les arguments à partir de l'indice 1 (on saute le nom du
# script) et on convertit chacun en entier.
nombres = [int(x) for x in sys.argv[1:]]

print(f"Nombre de valeurs : {len(nombres)}")
print(f"Somme             : {sum(nombres)}")
print(f"Minimum           : {min(nombres)}")
print(f"Maximum           : {max(nombres)}")
print(f"Valeurs triées    : {sorted(nombres)}")