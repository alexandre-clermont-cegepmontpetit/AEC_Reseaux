# ============================================================
# Révision Python - Fonctions
# ============================================================
#
# Consignes :
#
# Pour chaque exercice :
#
# 1. Compléter la fonction demandée.
# 2. Écrire le code de test sous la fonction.
# 3. Exécuter les tests afin de vérifier le bon
#    fonctionnement de votre solution.
#
# ============================================================
# Exercice 1 - Température extérieure
# ============================================================
#
# Écrire une fonction nommée description_temperature
# qui reçoit une température (nombre entier ou réel)
# et retourne :
#
# - "Très froid" si la température est inférieure à -10
# - "Froid" si la température est entre -10 et 9
# - "Doux" si la température est entre 10 et 24
# - "Chaud" si la température est supérieure ou égale à 25
#



# Données à utiliser pour les tests

temperatures = [-15, 5, 18, 30]

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec les températures
# contenues dans la liste temperatures.


# ============================================================
# Exercice 2 - Tarif de stationnement
# ============================================================
#
# Écrire une fonction nommée calculer_tarif
# qui reçoit la durée de stationnement en heures.
#
# La fonction doit retourner :
#
# - 5 $ pour moins de 2 heures
# - 10 $ pour une durée entre 2 et 5 heures inclusivement
# - 15 $ pour plus de 5 heures
#




# Données à utiliser pour les tests

durees = [1, 3, 8]

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec les durées
# contenues dans la liste durees.


# ============================================================
# Exercice 3 - Total des ventes
# ============================================================
#
# Écrire une fonction nommée total_ventes
# qui reçoit une liste contenant des montants de ventes.
#
# La fonction doit calculer et retourner
# la somme de tous les montants.
#
# Utiliser une boucle for.
#



# Données à utiliser pour les tests

ventes1 = [100, 50, 25]
ventes2 = [12.5, 10.5]
ventes3 = []

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec les listes
# ventes1, ventes2 et ventes3.


# ============================================================
# Exercice 4 - Compter les véhicules électriques
# ============================================================
#
# Écrire une fonction nommée compter_electriques
# qui reçoit une liste contenant les types de véhicules.
#
# La fonction doit retourner le nombre de véhicules
# électriques présents dans la liste.
#
# Utiliser une boucle for.
#




# Données à utiliser pour les tests

vehicules1 = [
    "electrique",
    "essence",
    "electrique",
    "hybride",
    "electrique"
]

vehicules2 = [
    "essence",
    "diesel"
]

vehicules3 = []

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec les listes
# vehicules1, vehicules2 et vehicules3.


# ============================================================
# Exercice 5 - Recherche d'un produit
# ============================================================
#
# Écrire une fonction nommée produit_existe
# qui reçoit :
#
# - une liste de produits
# - le nom d'un produit à rechercher
#
# La fonction retourne :
#
# - True si le produit existe dans la liste
# - False sinon
#
# Utiliser une boucle while.
#




# Données à utiliser pour les tests

produits = ["clavier", "ecran", "souris"]

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction en recherchant :
#
# - "ecran"
# - "imprimante"
# - "tablette" dans une liste vide


# ============================================================
# Exercice 6 - Description d'un animal
# ============================================================
#
# Écrire une fonction nommée description_animal
# qui reçoit un dictionnaire représentant un animal.
#
# Exemple :
#
# {
#     "nom": "Milo",
#     "espece": "Chat"
# }
#
# La fonction doit retourner une phrase comme :
#
# "Milo est un Chat."
#



# Données à utiliser pour les tests

animal1 = {
    "nom": "Milo",
    "espece": "Chat"
}

animal2 = {
    "nom": "Rex",
    "espece": "Chien"
}

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec animal1 et animal2.


# ============================================================
# Exercice 7 - Ajouter une catégorie à un colis
# ============================================================
#
# Écrire une fonction nommée ajouter_categorie
# qui reçoit un dictionnaire représentant un colis.
#
# Ajouter la clé "categorie" selon les règles suivantes :
#
# - moins de 1 kg : "Léger"
# - entre 1 et 5 kg inclusivement : "Moyen"
# - plus de 5 kg : "Lourd"
#
# Retourner le dictionnaire modifié.
#



# Données à utiliser pour les tests

colis1 = {"numero": 101, "poids": 0.5}
colis2 = {"numero": 102, "poids": 3}
colis3 = {"numero": 103, "poids": 8}

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec colis1, colis2
# et colis3.


# ============================================================
# Exercice 8 - Moyenne des températures
# ============================================================
#
# Écrire une fonction nommée moyenne_temperatures
# qui reçoit une liste de dictionnaires.
#
# Chaque dictionnaire contient :
#
# - ville
# - temperature
#
# La fonction retourne la température moyenne.
#
# Si la liste est vide, retourner 0.
#


# Données à utiliser pour les tests

mesures = [
    {"ville": "Montreal", "temperature": 18},
    {"ville": "Quebec", "temperature": 22},
    {"ville": "Sherbrooke", "temperature": 20},
    {"ville": "Gatineau", "temperature": 16}
]

mesure_unique = [
    {"ville": "Longueuil", "temperature": 19}
]

mesures_vides = []

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec :
#
# - mesures
# - mesure_unique
# - mesures_vides


# ============================================================
# Exercice 9 - Produits en rupture de stock
# ============================================================
#
# Écrire une fonction nommée produits_epuises
# qui reçoit une liste de dictionnaires représentant
# des produits.
#
# Retourner une nouvelle liste contenant seulement
# les produits dont la quantité est égale à 0.
#



# Données à utiliser pour les tests

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

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec :
#
# - produits1
# - produits2
# - produits3


# ============================================================
# Exercice 10 - Livre le plus récent
# ============================================================
#
# Écrire une fonction nommée livre_plus_recent
# qui reçoit une liste de dictionnaires représentant
# des livres.
#
# Chaque dictionnaire contient :
#
# - titre
# - annee
#
# La fonction retourne le dictionnaire correspondant
# au livre ayant l'année de publication la plus récente.
#
# Si la liste est vide, retourner None.
#



# Données à utiliser pour les tests

livres = [
    {"titre": "Python pour débutants", "annee": 2018},
    {"titre": "Administration Linux", "annee": 2021},
    {"titre": "Réseaux informatiques", "annee": 2019},
    {"titre": "Cybersécurité", "annee": 2024}
]

livre_unique = [
    {"titre": "PowerShell", "annee": 2022}
]

livres_vides = []

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec :
#
# - livres
# - livre_unique
# - livres_vides


# ============================================================
# Exercice 11 - Sauvegarde JSON
# ============================================================
#
# Écrire une fonction nommée sauvegarder_films
# qui reçoit :
#
# - un nom de fichier
# - une liste de dictionnaires représentant des films
#
# La fonction doit sauvegarder les données
# dans un fichier JSON.
#
# Utiliser le module json.
#



# Données à utiliser pour les tests

films = [
    {
        "titre": "Avatar",
        "annee": 2009,
        "realisateur": "James Cameron"
    },
    {
        "titre": "Dune",
        "annee": 2021,
        "realisateur": "Denis Villeneuve"
    },
    {
        "titre": "Interstellar",
        "annee": 2014,
        "realisateur": "Christopher Nolan"
    }
]

# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction.
#
# Vérifier également que le fichier JSON est bien créé.


# ============================================================
# Exercice 12 - Lecture JSON
# ============================================================
#
# Écrire une fonction nommée charger_films
# qui reçoit le nom d'un fichier JSON.
#
# La fonction doit lire le fichier et retourner
# son contenu.
#
# Utiliser le module json.
#



# Écrire le code de test nécessaire pour vérifier le bon
# fonctionnement de votre fonction avec le fichier créé
# à l'exercice précédent.

