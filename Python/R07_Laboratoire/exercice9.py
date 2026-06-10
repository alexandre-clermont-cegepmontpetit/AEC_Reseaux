# Exercice 9 - Retourner une nouvelle liste contenant seulement les nombres pairs

# Fonction de l'exercice 5
def est_pair(nombre):
    return nombre % 2 == 0


def obtenir_nombres_pairs(liste):
    nombres_pairs = []
    for nombre in liste:
        if est_pair(nombre):
            nombres_pairs.append(nombre)
    return nombres_pairs


# Test
nombres = [10, 7, 15, 22, 8, 13, 4]
nouvelle_liste = obtenir_nombres_pairs(nombres)

print(f"liste initiale : {nombres}")
print(f"nouvelle liste : {nouvelle_liste}")
