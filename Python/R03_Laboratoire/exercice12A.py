# Exercice 12A — Saisie sécurisée d’un mot de passe
mot_de_passe = "Passw0rd!"
saisie = input("Entrez le mot de passe : ")
while saisie != mot_de_passe:
    saisie = input("Entrez le mot de passe : ")
print("Accès autorisé.")