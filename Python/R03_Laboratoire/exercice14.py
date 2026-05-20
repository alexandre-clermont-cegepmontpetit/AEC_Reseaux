# Exercice 14 — Lecture continue des logs système
logs = ["INFO", "INFO", "WARNING", "INFO", "ERREUR", "INFO"]
for message in logs:
    if message == "ERREUR":
        print("ERREUR détectée — arrêt de la lecture.")
        break
    print(f"Log lu : {message}")