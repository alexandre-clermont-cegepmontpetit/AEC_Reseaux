# Exercice 4 - Conversion de température

def celsius_vers_fahrenheit(celsius):
    return 9 / 5 * celsius + 32


# Demander une température à l'utilisateur
celsius = float(input("Entrez une température en Celsius : "))

# Appeler la fonction
fahrenheit = celsius_vers_fahrenheit(celsius)

# Afficher le résultat
print(f"{celsius} °C = {fahrenheit} °F")
