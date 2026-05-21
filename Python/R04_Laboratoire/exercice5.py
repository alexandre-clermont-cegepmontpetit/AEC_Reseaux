# Exercice 5 — Liste dans un dictionnaire

# Création du dictionnaire switch
switch = {
    "hostname": "SW1",
    "vlans": [5, 10, 20, 30, 50, 4095]
}

# Afficher le nom du switch et tous les VLANs
print("=== SWITCH INITIAL ===")
print("Hostname :", switch["hostname"])
print("VLANs :", switch["vlans"])

# Ajouter un VLAN à la liste
print("\n=== APRÈS AJOUT DU VLAN 40 ===")
switch["vlans"].append(40)
print("VLANs :", switch["vlans"])

# Supprimer un VLAN spécifique
print("\n=== APRÈS SUPPRESSION DU VLAN 20 ===")
switch["vlans"].remove(20)
print("VLANS :", switch["vlans"])

# Vérifier si un VLAN spécifique existe
if 30 in switch["vlans"]:
    print("\nLe VLAN 30 existe dans la liste.")
else:
    print("\nLe VLAN 30 n'existe pas dans la liste.")

# Afficher le nombre total de VLANs
print("\nNombre total de VLANs :", len(switch["vlans"]))

# Parcourir et afficher chaque VLAN individuellement
print("\n=== PARCOURS DES VLANs ===")
for vlan in switch["vlans"]:
    print("VLAN", ":", vlan)

# Vérifier que chaque VLAN est dans la plage autorisée (10 à 100)
print("\n=== VÉRIFICATION DES VLANs DANS LA PLAGE 10-100 ===")
for vlan in switch["vlans"]:
    if 10 <= vlan <= 100:
        print("VLAN", vlan, "✅ autorisé")
    else:
        print("VLAN", vlan, "❌ hors plage autorisée")
