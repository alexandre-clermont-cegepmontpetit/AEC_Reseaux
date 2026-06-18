# Exercice 4
# Reçoit le nom d'un étudiant suivi d'une série de notes, puis affiche le nom,
# le nombre de notes, la moyenne, la note minimale et la note maximale.
# Utilisation :
#     python3 notes_etudiant.py Sophie 85 92 78 90
import sys

if len(sys.argv) < 3:
    print("Utilisation : python notes_etudiant.py <nom> <note1> <note2> ...")
    sys.exit(1)

# Le premier argument est le nom de l'étudiant.
nom = sys.argv[1]

# Les notes commencent à l'indice 2 (juste après le nom).
notes = [int(x) for x in sys.argv[2:]]

moyenne = sum(notes) / len(notes)

print(f"Étudiant        : {nom}")
print(f"Nombre de notes : {len(notes)}")
print(f"Moyenne         : {moyenne:.2f}")
print(f"Note minimale   : {min(notes)}")
print(f"Note maximale   : {max(notes)}")