# Exercice 11 - Afficher une liste de dictionnaires

# Fonction de l'exercice 10
def afficher_dictionnaire(dictionnaire):
    for cle, valeur in dictionnaire.items():
        print(f"{cle} : {valeur}")


def afficher_liste_dictionnaires(liste_dictionnaires):
    for dictionnaire in liste_dictionnaires:
        afficher_dictionnaire(dictionnaire)  # réutilisation de la fonction
        print("-------------------")


# Test
etudiants = [
    {"nom": "Alice", "age": 20, "programme": "Informatique"},
    {"nom": "Bob", "age": 22, "programme": "Cybersécurité"},
    {"nom": "Charlie", "age": 19, "programme": "Réseaux"}
]

afficher_liste_dictionnaires(etudiants)
