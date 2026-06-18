import json

with open("data1.json", "r", encoding="utf-8") as fichier:
    etudiant=json.load(fichier)

print(etudiant)