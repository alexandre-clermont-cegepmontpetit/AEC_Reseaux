# Exercice 6 — Température

temperature = float(input("Entrez la température : "))

if temperature < 0:
    print("Il gèle dehors")
elif temperature <= 25:
    print("Température agréable")
else:
    print("Il fait chaud")
