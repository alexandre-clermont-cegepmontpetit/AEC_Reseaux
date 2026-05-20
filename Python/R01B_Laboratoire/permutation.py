# Permute les valeurs de deux nombres (A et B) saisis par l'utilisateur

# Saisie des deux nombres
a = input("Entrez la valeur de A : ")
b = input("Entrez la valeur de B : ")

# Permutation des variables
a, b = b, a

# Affichage
print("Nouvelles valeurs: A=" + a + " et B=" + b)