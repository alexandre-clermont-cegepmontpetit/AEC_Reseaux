# Exercice 10 - Afficher le contenu d'un dictionnaire

def afficher_dictionnaire(dictionnaire):
    for cle, valeur in dictionnaire.items():
        print(f"{cle} : {valeur}")


# Test
etudiant = {
    "nom": "Alice",
    "age": 20,
    "programme": "Informatique"
}

afficher_dictionnaire(etudiant)
