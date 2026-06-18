import json

with open("data4.json", "r", encoding="utf-8") as fichier:
    etudiants = json.load(fichier)

for etudiant in etudiants:
    print(etudiant["nom"], ":", etudiant["note"])