# Exercice 10 — Vérification des sauvegardes automatiques
sauvegardes = [True, False, True, True, False]
reussies = 0
for s in sauvegardes:
    if s == True:
        reussies += 1
print(f"Nombre de sauvegardes réussies : {reussies}")