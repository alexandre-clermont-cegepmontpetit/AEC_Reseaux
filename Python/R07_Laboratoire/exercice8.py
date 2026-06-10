# Exercice 8 - Faire la somme des éléments d'une liste

def calculer_somme(liste):
    somme = 0
    for nombre in liste:
        somme = somme + nombre
    return somme


# Tests avec deux listes
liste1 = [10, 20, 30, 40]
liste2 = [-10, 20, 30, 40]

print(f"La somme est : {calculer_somme(liste1)}")
print(f"La somme est : {calculer_somme(liste2)}")
