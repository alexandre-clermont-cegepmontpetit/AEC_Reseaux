# Exercice 5 - Vérification d'un nombre pair

def est_pair(nombre):
    # Le reste de la division par 2 est 0 si le nombre est pair
    return nombre % 2 == 0


# Tests avec plusieurs nombres
print(f"5 est pair : {est_pair(5)}")
print(f"10 est pair : {est_pair(10)}")
