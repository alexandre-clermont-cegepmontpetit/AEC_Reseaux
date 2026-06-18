import json

etudiant = {
    "nom": "Sophie",
    "age": 22,
    "programme": "Réseautique"
}

with open("data2.json", "w", encoding="utf-8") as fichier:
    etudiant=json.dump(etudiant, fichier)