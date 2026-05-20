# Exercice 5 — Vérification d’un processus sur deux (indices pairs)
pids = [101, 102, 103, 104, 105]
for i in range(len(pids)):
    if i % 2 == 0:
        print(f"Indice {i} : PID {pids[i]}")