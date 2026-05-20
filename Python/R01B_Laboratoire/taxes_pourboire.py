# Calcule les montants des taxes (15 %) et du pourboire (10 %) à partir du prix d'un repas

# Saisie du prix du repas
prix_repas = float(input("Prix du repas : "))

# Calculs des taxes et du pourboire
taxes = prix_repas * 0.15
pourboire = prix_repas * 0.1

# Calcul du total à payer
total = prix_repas + taxes + pourboire

# Affichage
print("Total à payer : " + str(total))