import json

etudiant = {
    "nom": "Sophie",
    "age": 22,
    "programme": "Réseautique"
}

with open("data3.json", "w", encoding="utf-8") as fichier:
    etudiant=json.dump(etudiant, fichier, indent=4)