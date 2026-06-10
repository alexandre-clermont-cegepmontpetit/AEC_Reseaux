# Exercice 7 - Afficher le contenu d'une liste

def afficher_liste(liste):
    for element in liste:
        print(element)


# Tests avec deux listes
noms = ["Alice", "Bob", "Charlie", "David"]
nombres = [10, 20, 30, 40]

afficher_liste(noms)
afficher_liste(nombres)
