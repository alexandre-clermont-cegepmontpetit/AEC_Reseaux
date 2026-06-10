# Exercice 3 - Calculer le total de plusieurs nombres

def addition(nombre1, nombre2):
    return nombre1 + nombre2


# Total de 2 nombres
total = addition(7, 12)
print(f"Total : {total}")

# Total de 3 nombres : on réutilise la fonction
# addition(5, 10) donne 15, puis addition(15, 20) donne 35
total = addition(addition(5, 10), 20)
print(f"Total : {total}")

# Total de 4 nombres : même principe
total = addition(addition(addition(3, 15), 7), 20)
print(f"Total : {total}")
