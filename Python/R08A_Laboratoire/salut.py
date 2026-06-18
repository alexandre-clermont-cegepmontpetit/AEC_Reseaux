# Exercice 1
# Reçoit un nom en paramètre et affiche : Bonjour nom !
# Utilisation :
#     python3 salut.py Jamil
import sys

# sys.argv[0] est le nom du script, sys.argv[1] est le premier argument fourni.
if len(sys.argv) != 2:
    print("Utilisation : python salut.py <nom>")
    sys.exit(1)

nom = sys.argv[1]
print(f"Bonjour {nom} !")
