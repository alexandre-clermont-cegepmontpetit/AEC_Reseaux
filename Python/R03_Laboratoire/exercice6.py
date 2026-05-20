# Exercice 6 — Mise à jour de l’espace disque (+10 Go)
espaces = [101, 102, 103, 104, 105]
for i in range(len(espaces)):
    ancien = espaces[i]
    espaces[i] = ancien + 10
    print(f"Ancien espace : {ancien} Go  ->  Nouvel espace : {espaces[i]} Go")