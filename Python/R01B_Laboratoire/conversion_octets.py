# Calcule le nombre de mégaoctets, kilo-octets et des octets restants à partir d'un nombre d'octets

octets_total = int(input("Entrez le nombre d'octets : "))

# Constante de conversion
C = 1024

# Calcul des mégaoctets et du reste
mo = octets_total // (C * C)
reste = octets_total % (C * C)

# Calcul des kilo-octets et des octets restants
ko = reste // C
octets = reste % C

# Affichage
print(str(mo) + " Mo, " + str(ko) + " Ko et " + str(octets) + " octets")