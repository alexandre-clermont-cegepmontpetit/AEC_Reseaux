# Exercice 6 - Calcul de l'aire d'un rectangle

def calculer_aire_rectangle(longueur, largeur):
    return longueur * largeur


# Demander les dimensions à l'utilisateur
longueur = float(input("Entrez la longueur : "))
largeur = float(input("Entrez la largeur : "))

# Appeler la fonction
aire = calculer_aire_rectangle(longueur, largeur)

# Afficher le résultat
print(f"L'aire du rectangle est : {aire}")
