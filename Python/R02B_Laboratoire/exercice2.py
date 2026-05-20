# Exercice 2 — Avancer d'une seconde
# Demande l'heure actuelle (heures, minutes, secondes) et affiche
# l'heure exactement une seconde plus tard.

# Saisie de l'heure actuelle
heures = int(input("Entrez les heures (0-23) : "))
minutes = int(input("Entrez les minutes (0-59) : "))
secondes = int(input("Entrez les secondes (0-59) : "))

# Ajout d'une seconde avec gestion des dépassements
secondes += 1

# Si les secondes atteignent 60, on incrémente les minutes
if secondes == 60:
    secondes = 0
    minutes += 1

    # Si les minutes atteignent 60, on incrémente les heures
    if minutes == 60:
        minutes = 0
        heures += 1

        # Si les heures atteignent 24, on revient à 0 (minuit)
        if heures == 24:
            heures = 0

# Affichage avec format à deux chiffres (ex : 09:05:03)
print(f"Une seconde plus tard, il sera : {heures:02d}:{minutes:02d}:{secondes:02d}")

# Cas de test (affichage à deux chiffres): 0, 0, 0
# Cas de test (cas spécial - retour à 00:00:00): 23, 59, 59