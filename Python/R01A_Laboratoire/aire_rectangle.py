# Calcule la superficie occupée par des racks dans un centre de données

# Saisie utilisateur
longueur_str = input("Saisir la longueur du rectangle (m) : ")
largeur_str = input("Saisir la largeur du rectangle (m) : ")

# Conversion en float
longueur = float(longueur_str)
largeur = float(largeur_str)

# Calcul de l'aire
aire = longueur * largeur

# Affichage
print("---------------------------------")
print("Le calcul est terminé.")
print("L'aire totale du rectangle est : " + str(aire) + " m²")