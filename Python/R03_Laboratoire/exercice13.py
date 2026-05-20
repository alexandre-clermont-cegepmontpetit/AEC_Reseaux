# Exercice 13 — Surveillance de l’utilisation CPU
cpu = 95
print(f"Charge CPU initiale : {cpu} %")
while cpu > 80:
    print(f"Alerte CPU : {cpu} %")
    cpu -= 5
print("Charge CPU redevenue normale.")