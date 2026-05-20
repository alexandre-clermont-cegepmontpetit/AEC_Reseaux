# Convertit Mbps en Mo/s et calcule un temps de téléchargement

# Vitesse annoncée du lien
vitesse_mbps = 500

# Conversion Mbps -> Mo/s (1 octet = 8 bits)
vitesse_mo_s = vitesse_mbps / 8

# Calcul du temps pour télécharger 1000 Mo
taille_fichier_mo = 1000
temps_secondes = taille_fichier_mo / vitesse_mo_s

# Affichage
print("--- ANALYSE DE LA LIGNE ---")
print("Vitesse : " + str(vitesse_mo_s) + " Mo/s")
print("Temps estimé pour 1000 Mo : " + str(temps_secondes) + " secondes")