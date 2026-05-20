# Calcule le nombre d'heures et de jours complets à partir d'un nombre de minutes

# Saisie du nombre de minutes
minutes = int(input("Minutes : "))

# Calcul du nombre d'heures et de jours complets
heures = minutes // 60
jours = heures // 24

# Affichage
print("Heures : " + str(heures))
print("Jours : " + str(jours))