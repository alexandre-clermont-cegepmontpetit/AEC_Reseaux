# Exercice 11 — Analyse de l’utilisation mémoire
memoires = [1024, 2048, 3072, 4096, 5120]
somme = 0
for m in memoires:
    somme += m
moyenne = somme / len(memoires)
print(f"Mémoire totale : {somme} Mo")
print(f"Moyenne : {moyenne} Mo")