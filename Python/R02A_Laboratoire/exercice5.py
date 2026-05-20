# Exercice 5 — Code secret

prenom = input("Entrez votre prénom : ")
code = int(input("Entrez votre code secret : "))

if prenom == "Alice" and code == 1234:
    print("Accès accordé")
else:
    print("Accès refusé")
