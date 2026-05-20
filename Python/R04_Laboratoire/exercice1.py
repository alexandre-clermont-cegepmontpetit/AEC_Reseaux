# Exercice 1 — Créer et manipuler un dictionnaire

# Création du dictionnaire
routeur = {
    "hostname": "R1",
    "ip": "192.168.1.1",
    "os": "Cisco IOS"
}

# Afficher le dictionnaire au complet
print("=== AFFICHAGE DU DICTIONNAIRE ===")
print(routeur)

# Afficher le nombre de clés
print("\n" + "Nombre de clés dans le dictionnaire :", len(routeur))

# Afficher chaque clé une par une
print("\n" + "=== VALEUR DE CHAQUE CLÉ ===")
print("Hostname :", routeur["hostname"])
print("IP       :", routeur["ip"])
print("OS       :", routeur["os"])

# Modifier l'adresse IP
routeur["ip"] = "10.0.0.1"
print("\n" + "=== APRÈS MODIFICATION (IP changée) ===")
print("Nouvelle IP :", routeur["ip"])
print(routeur)

# Ajouter une nouvelle clé
routeur["ssh"] = True
cle_ajoutee, valeur_ajoutee = next(reversed(routeur.items()))
print("\n" + "=== APRÈS AJOUT D'UNE CLÉ ===")
print("Clé ajoutée : '" + cle_ajoutee + "'", "=", valeur_ajoutee)
print(routeur)

# Supprimer la clé os
del routeur["os"]
print("\n" + "=== VÉRIFICATION SI LA CLÉ EXISTE ENCORE ===")
try:
    value = routeur["os"]   # KeyError: 'os' does not exist
except KeyError as e:
    print("La clé n'existe pas")
print(routeur)

# Parcourir les clés et afficher chaque clé avec sa valeur
print("\n" + "=== PARCOURS DS CLÉS ===")
for cle, valeur in routeur.items():
    print(cle, "->", valeur)

# Vider le dictionnaire
routeur.clear()
print("\n" + "=== APRÈS VIDAGE DU DICTIONNAIRE ===")
print(routeur)
