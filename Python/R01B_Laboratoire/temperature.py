# Convertit la température saisie par l'utilisateur (nombre décimal) de Celsius à Fahrenheit

# Saisie de la température en Celsius
celsius = float(input("Température : "))

# Conversion de Celsius à Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Affichage
print("En Fahrenheit : " + str(fahrenheit))