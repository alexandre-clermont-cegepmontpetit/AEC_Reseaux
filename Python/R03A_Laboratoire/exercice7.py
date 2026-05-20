# Exercice 7 — Augmenter la mémoire RAM (+512 Mo)
memoires = [1024, 2048, 3072, 4096, 5120]
for i in range(len(memoires)):
    ancienne = memoires[i]
    memoires[i] = ancienne + 512
    print(f"Ancienne RAM : {ancienne} Mo  ->  Nouvelle RAM : {memoires[i]} Mo")