# Exercice 9 — Comptage de processus récents (PID > 103)
pids = [101, 102, 103, 104, 105]
compteur = 0
for pid in pids:
    if pid > 103:
        compteur += 1
print(f"Nombre de PID > 103 : {compteur}")