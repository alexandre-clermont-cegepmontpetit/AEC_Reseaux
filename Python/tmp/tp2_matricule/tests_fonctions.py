"""
Fichier : tests_fonctions.py

Objectif :
    Tester progressivement les fonctions du gestionnaire de tâches.

Consignes :
    1. Développez une fonction dans le fichier fonctions_taches.py.
    2. Exécutez ce fichier de tests.
    3. Vérifiez que le résultat obtenu correspond au résultat attendu.
    4. Corrigez les erreurs au besoin.
    5. Passez ensuite à la fonction suivante.

Exécution :
    python3 tests_fonctions.py
"""

from fonctions_taches import *


# ==========================
# Données de test
# ==========================

taches = [
    {
        "titre": "Faire le TP Python",
        "priorite": 1,
        "categorie": "Cours",
        "terminee": False
    },
    {
        "titre": "Acheter du lait",
        "priorite": 3,
        "categorie": "Personnel",
        "terminee": False
    },
    {
        "titre": "Préparer la réunion",
        "priorite": 2,
        "categorie": "Travail",
        "terminee": True
    }
]


# ==========================================================
# TEST 1 : ajouter_tache
# ==========================================================

print("\n" + "=" * 60)
print("TEST 1 - ajouter_tache")
print("=" * 60)

print("""
Objectif :
    Ajouter une nouvelle tâche dans la liste.

Résultat attendu :
    Une nouvelle tâche intitulée 'Réviser Python'
    doit être ajoutée à la fin de la liste.
""")

ajouter_tache(
    taches,
    "Réviser Python",
    1,
    "Cours"
)

afficher_taches(taches)


# ==========================================================
# TEST 2 : rechercher_tache
# ==========================================================

print("\n" + "=" * 60)
print("TEST 2 - rechercher_tache")
print("=" * 60)

print("""
Objectif :
    Rechercher une tâche existante.

Résultat attendu :
    La tâche 'Acheter du lait' doit être retournée.
""")

resultat = rechercher_tache(
    taches,
    "Acheter du lait"
)

print(resultat)

print("\nRecherche d'une tâche inexistante")

print("""
Résultat attendu :
    La fonction doit retourner None.
""")

resultat = rechercher_tache(
    taches,
    "Tâche inexistante"
)

print(resultat)


# ==========================================================
# TEST 3 : terminer_tache
# ==========================================================

print("\n" + "=" * 60)
print("TEST 3 - terminer_tache")
print("=" * 60)

print("""
Objectif :
    Marquer une tâche comme terminée.

Résultat attendu :
    La tâche 'Faire le TP Python'
    doit maintenant être affichée comme terminée.
""")

terminer_tache(
    taches,
    "Faire le TP Python"
)

afficher_taches(taches)


# ==========================================================
# TEST 4 : filtrer_par_categorie
# ==========================================================

print("\n" + "=" * 60)
print("TEST 4 - filtrer_par_categorie")
print("=" * 60)

print("""
Objectif :
    Obtenir uniquement les tâches de la catégorie 'Cours'.

Résultat attendu :
    Seules les tâches dont la catégorie est 'Cours'
    doivent être affichées.
""")

taches_cours = filtrer_par_categorie(
    taches,
    "Cours"
)

afficher_taches(taches_cours)


# ==========================================================
# TEST 5 : statistiques
# ==========================================================

print("\n" + "=" * 60)
print("TEST 5 - statistiques")
print("=" * 60)

print("""
Objectif :
    Afficher les statistiques des tâches.

Résultat attendu :
    Affichage :
        - nombre total de tâches
        - nombre de tâches terminées
        - nombre de tâches non terminées
""")

statistiques(taches)


# ==========================================================
# TEST 6 : sauvegarder_taches
# ==========================================================

print("\n" + "=" * 60)
print("TEST 6 - sauvegarder_taches")
print("=" * 60)

print("""
Objectif :
    Sauvegarder les tâches dans un fichier JSON.

Résultat attendu :
    Le fichier taches_test.json doit être créé.
""")

sauvegarder_taches(
    taches,
    "taches_test.json"
)

print("Vérifiez la présence du fichier taches_test.json.")


# ==========================================================
# TEST 7 : charger_taches
# ==========================================================

print("\n" + "=" * 60)
print("TEST 7 - charger_taches")
print("=" * 60)

print("""
Objectif :
    Charger les tâches à partir du fichier JSON.

Résultat attendu :
    Les tâches précédemment sauvegardées
    doivent être affichées.
""")

taches_chargees = charger_taches(
    "taches_test.json"
)

afficher_taches(taches_chargees)


# ==========================================================
# TEST 8 : sauvegarder_par_categorie
# ==========================================================

print("\n" + "=" * 60)
print("TEST 8 - sauvegarder_par_categorie")
print("=" * 60)

print("""
Objectif :
    Créer un fichier JSON par catégorie.

Résultat attendu :
    Des fichiers tels que :

        Cours.json
        Personnel.json
        Travail.json

    doivent être créés.
""")

sauvegarder_par_categorie(
    taches
)

print("Vérifiez les fichiers JSON générés.")


# ==========================================================
# FIN DES TESTS
# ==========================================================

print("\n" + "=" * 60)
print("FIN DES TESTS")
print("=" * 60)

print("""
Si tous les tests fonctionnent correctement :

1. Les fonctions sont terminées.
2. Vous pouvez maintenant utiliser le programme principal.
3. Vous pouvez remplacer les données hardcodées
   par le chargement à partir d'un fichier JSON.
""")