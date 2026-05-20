# Exercice 15 — Vérification d’espace disque
espace = 30  # Go disponibles au départ
print(f"Espace disponible initialement : {espace} Go")
while espace < 50:
    espace += 5
    print(f"Nettoyage en cours...\nEspace disponible : {espace} Go")
print("Espace disque suffisant.")