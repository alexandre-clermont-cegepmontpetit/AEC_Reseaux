# ============================================================
# Révision Python - Fonctions  (SOLUTIONS)
# ============================================================

import json


# ============================================================
# Exercice 1 - Température extérieure
# ============================================================
# < -10 : "Très froid" | -10 à 9 : "Froid"
# 10 à 24 : "Doux"     | >= 25   : "Chaud"

def description_temperature(temperature):
    if temperature < -10:
        return "Très froid"
    elif temperature < 10:
        return "Froid"
    elif temperature < 25:
        return "Doux"
    else:
        return "Chaud"


temperatures = [-15, 5, 18, 30]

print("--- Exercice 1 ---")
for t in temperatures:
    print(t, "->", description_temperature(t))
print()


# ============================================================
# Exercice 2 - Tarif de stationnement
# ============================================================
# < 2 h : 5 $ | 2 à 5 h : 10 $ | > 5 h : 15 $

def calculer_tarif(duree):
    if duree < 2:
        return 5
    elif duree <= 5:
        return 10
    else:
        return 15


durees = [1, 3, 8]

print("--- Exercice 2 ---")
for d in durees:
    print(d, "h ->", calculer_tarif(d), "$")
print()


# ============================================================
# Exercice 3 - Total des ventes
# ============================================================

def total_ventes(ventes):
    total = 0
    for montant in ventes:
        total += montant
    return total


ventes1 = [100, 50, 25]
ventes2 = [12.5, 10.5]
ventes3 = []

print("--- Exercice 3 ---")
print(total_ventes(ventes1))
print(total_ventes(ventes2))
print(total_ventes(ventes3))
print()


# ============================================================
# Exercice 4 - Compter les véhicules électriques
# ============================================================

def compter_electriques(vehicules):
    compteur = 0
    for vehicule in vehicules:
        if vehicule == "electrique":
            compteur += 1
    return compteur


vehicules1 = ["electrique", "essence", "electrique", "hybride", "electrique"]
vehicules2 = ["essence", "diesel"]
vehicules3 = []

print("--- Exercice 4 ---")
print(compter_electriques(vehicules1))
print(compter_electriques(vehicules2))
print(compter_electriques(vehicules3))
print()


# ============================================================
# Exercice 5 - Recherche d'un produit  (boucle while)
# ============================================================

def produit_existe(produits, nom):
    i = 0
    while i < len(produits):
        if produits[i] == nom:
            return True
        i += 1
    return False


produits = ["clavier", "ecran", "souris"]

print("--- Exercice 5 ---")
print(produit_existe(produits, "ecran"))
print(produit_existe(produits, "imprimante"))
print(produit_existe([], "tablette"))
print()


# ============================================================
# Exercice 6 - Description d'un animal
# ============================================================

def description_animal(animal):
    return f"{animal['nom']} est un {animal['espece']}."


animal1 = {"nom": "Milo", "espece": "Chat"}
animal2 = {"nom": "Rex", "espece": "Chien"}

print("--- Exercice 6 ---")
print(description_animal(animal1))
print(description_animal(animal2))
print()


# ============================================================
# Exercice 7 - Ajouter une catégorie à un colis
# ============================================================
# < 1 kg : "Léger" | 1 à 5 kg : "Moyen" | > 5 kg : "Lourd"

def ajouter_categorie(colis):
    poids = colis["poids"]
    if poids < 1:
        colis["categorie"] = "Léger"
    elif poids <= 5:
        colis["categorie"] = "Moyen"
    else:
        colis["categorie"] = "Lourd"
    return colis


colis1 = {"numero": 101, "poids": 0.5}
colis2 = {"numero": 102, "poids": 3}
colis3 = {"numero": 103, "poids": 8}

print("--- Exercice 7 ---")
print(ajouter_categorie(colis1))
print(ajouter_categorie(colis2))
print(ajouter_categorie(colis3))
print()


# ============================================================
# Exercice 8 - Moyenne des températures
# ============================================================

def moyenne_temperatures(mesures):
    if len(mesures) == 0:
        return 0
    total = 0
    for mesure in mesures:
        total += mesure["temperature"]
    return total / len(mesures)


mesures = [
    {"ville": "Montreal", "temperature": 18},
    {"ville": "Quebec", "temperature": 22},
    {"ville": "Sherbrooke", "temperature": 20},
    {"ville": "Gatineau", "temperature": 16}
]
mesure_unique = [{"ville": "Longueuil", "temperature": 19}]
mesures_vides = []

print("--- Exercice 8 ---")
print(moyenne_temperatures(mesures))
print(moyenne_temperatures(mesure_unique))
print(moyenne_temperatures(mesures_vides))
print()


# ============================================================
# Exercice 9 - Produits en rupture de stock
# ============================================================

def produits_epuises(produits):
    epuises = []
    for produit in produits:
        if produit["quantite"] == 0:
            epuises.append(produit)
    return epuises


produits1 = [
    {"nom": "Clavier", "quantite": 5},
    {"nom": "Souris", "quantite": 0},
    {"nom": "Écran", "quantite": 3},
    {"nom": "Webcam", "quantite": 0},
    {"nom": "Casque", "quantite": 8}
]
produits2 = [
    {"nom": "Routeur", "quantite": 5},
    {"nom": "Switch", "quantite": 2}
]
produits3 = []

print("--- Exercice 9 ---")
print(produits_epuises(produits1))
print(produits_epuises(produits2))
print(produits_epuises(produits3))
print()


# ============================================================
# Exercice 10 - Livre le plus récent
# ============================================================

def livre_plus_recent(livres):
    if len(livres) == 0:
        return None
    plus_recent = livres[0]
    for livre in livres:
        if livre["annee"] > plus_recent["annee"]:
            plus_recent = livre
    return plus_recent


livres = [
    {"titre": "Python pour débutants", "annee": 2018},
    {"titre": "Administration Linux", "annee": 2021},
    {"titre": "Réseaux informatiques", "annee": 2019},
    {"titre": "Cybersécurité", "annee": 2024}
]
livre_unique = [{"titre": "PowerShell", "annee": 2022}]
livres_vides = []

print("--- Exercice 10 ---")
print(livre_plus_recent(livres))
print(livre_plus_recent(livre_unique))
print(livre_plus_recent(livres_vides))
print()


# ============================================================
# Exercice 11 - Sauvegarde JSON
# ============================================================

def sauvegarder_films(nom_fichier, films):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(films, f, ensure_ascii=False, indent=4)


films = [
    {"titre": "Avatar", "annee": 2009, "realisateur": "James Cameron"},
    {"titre": "Dune", "annee": 2021, "realisateur": "Denis Villeneuve"},
    {"titre": "Interstellar", "annee": 2014, "realisateur": "Christopher Nolan"}
]

print("--- Exercice 11 ---")
sauvegarder_films("films.json", films)
print("Fichier films.json créé avec succès.")
print()


# ============================================================
# Exercice 12 - Lecture JSON
# ============================================================

def charger_films(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return json.load(f)


print("--- Exercice 12 ---")
donnees = charger_films("films.json")
for film in donnees:
    print(film)
