# Exercice 12B — Saisie sécurisée (3 tentatives maximum)
mot_de_passe = "Passw0rd!"
tentatives = 0
acces = False
while tentatives < 3:
    saisie = input("Entrer le mot de passe : ")
    if saisie == mot_de_passe:
        print("Accès autorisé.")
        acces = True
        break
    else:
        tentatives += 1
        print("Mot de passe incorrect.")

if not acces:
    print("Accès bloqué après 3 tentatives.")