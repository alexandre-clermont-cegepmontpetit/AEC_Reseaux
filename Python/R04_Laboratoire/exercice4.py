# Exercice 4 — Liste de processus

# Création de la liste de dictionnaires
processus = [
    {"pid": 101, "nom": "sshd",   "utilisateur": "root",  "en_cours": True},
    {"pid": 102, "nom": "chrome", "utilisateur": "alice", "en_cours": True},
    {"pid": 103, "nom": "python", "utilisateur": "bob",   "en_cours": False},
    {"pid": 104, "nom": "nginx",  "utilisateur": "root",  "en_cours": True},
    {"pid": 105, "nom": "code",   "utilisateur": "alice", "en_cours": False}
]

# Afficher tous les processus
print("Tous les processus :")
for p in processus:
    print(p)

# Afficher seulement les processus en cours
print("\nProcessus en cours :")
for p in processus:
    if p["en_cours"]:
        print(p["pid"], "-", p["nom"])

# Calculer le nombre de processus actifs
nb_actifs = 0
for p in processus:
    if p["en_cours"]:
        nb_actifs += 1
print("\nNombre de processus actifs :", nb_actifs)

# Calculer le nombre de processus exécutés par root
nb_root = 0
for p in processus:
    if p["utilisateur"] == "root":
        nb_root += 1
print("Nombre de processus exécutés par root :", nb_root)
