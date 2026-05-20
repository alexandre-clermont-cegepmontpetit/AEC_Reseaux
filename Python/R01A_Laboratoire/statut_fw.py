# Tableau de bord de surveillance pour pare-feu

# Variables
nom_firewall = "FW-SÉCURITÉ-01"        # str
connexions_bloquees = 1250             # int
charge_cpu = 14.2                      # float
mode_alerte = False                    # bool

# Affichage
print("STATUT DU PARE-FEU : " + nom_firewall)
print("Connexions bloquées : " + str(connexions_bloquees))
print("Charge CPU : " + str(charge_cpu) + " %")
print("Mode Alerte critique : " + str(mode_alerte))