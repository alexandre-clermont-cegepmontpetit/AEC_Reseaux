# ============================================================
# Laboratoire 3 : Listes et boucles
# ============================================================

# ------------------------------------------------------------
# PARCOURS DE LISTE
# ------------------------------------------------------------

# Exercice 1 — Affichage des processus actifs Linux
pids = [101, 102, 103, 104, 105]
for pid in pids:
    print(pid)


# Exercice 2 — Affichage des positions des processus
pids = [101, 102, 103, 104, 105]
for i in range(len(pids)):
    print(f"Indice {i} : PID {pids[i]}")
# Variante avec enumerate :
# for i, pid in enumerate(pids):
#     print(f"Indice {i} : PID {pid}")


# ------------------------------------------------------------
# FILTRAGE DE LISTE
# ------------------------------------------------------------

# Exercice 3 — Processus lancés récemment (PID > 102)
pids = [101, 102, 103, 104, 105]
for pid in pids:
    if pid > 102:
        print(pid)


# Exercice 4 — Processus système pairs
pids = [101, 102, 103, 104, 105]
for pid in pids:
    if pid % 2 == 0:
        print(pid)


# Exercice 5 — Vérification d’un processus sur deux (indices pairs)
pids = [101, 102, 103, 104, 105]
for i in range(len(pids)):
    if i % 2 == 0:
        print(f"Indice {i} : PID {pids[i]}")


# ------------------------------------------------------------
# TRANSFORMATION ET CALCUL
# ------------------------------------------------------------

# Exercice 6 — Mise à jour de l’espace disque (+10 Go)
espaces = [101, 102, 103, 104, 105]
for i in range(len(espaces)):
    ancien = espaces[i]
    espaces[i] = ancien + 10
    print(f"Ancien espace : {ancien} Go  ->  Nouvel espace : {espaces[i]} Go")


# Exercice 7 — Augmenter la mémoire RAM (+512 Mo)
memoires = [1024, 2048, 3072, 4096, 5120]
for i in range(len(memoires)):
    ancienne = memoires[i]
    memoires[i] = ancienne + 512
    print(f"Ancienne RAM : {ancienne} Mo  ->  Nouvelle RAM : {memoires[i]} Mo")


# ------------------------------------------------------------
# BOUCLE WHILE ET BREAK
# ------------------------------------------------------------

# Exercice 8 — Compte à rebours avant redémarrage
temps = 5
while temps > 0:
    print(f"Attention : redémarrage dans {temps} seconde(s)...")
    temps -= 1
print("Le serveur redémarre maintenant.")


# Exercice 9 — Comptage de processus récents (PID > 103)
pids = [101, 102, 103, 104, 105]
compteur = 0
for pid in pids:
    if pid > 103:
        compteur += 1
print(f"Nombre de PID supérieurs à 103 : {compteur}")


# ------------------------------------------------------------
# CALCUL ET STATISTIQUES
# ------------------------------------------------------------

# Exercice 10 — Vérification des sauvegardes automatiques
sauvegardes = [True, False, True, True, False]
reussies = 0
for s in sauvegardes:
    if s == True:
        reussies += 1
print(f"Nombre de sauvegardes réussies : {reussies}")


# Exercice 11 — Analyse de l’utilisation mémoire
memoires = [1024, 2048, 3072, 4096, 5120]
somme = 0
for m in memoires:
    somme += m
moyenne = somme / len(memoires)
print(f"Somme totale : {somme} Mo")
print(f"Moyenne d'utilisation : {moyenne} Mo")


# Exercice 12A — Saisie sécurisée d’un mot de passe
mot_de_passe = "admin123"
saisie = input("Entrez le mot de passe : ")
while saisie != mot_de_passe:
    print("Mot de passe incorrect.")
    saisie = input("Entrez le mot de passe : ")
print("Accès autorisé.")


# Exercice 12B — Saisie sécurisée (3 tentatives maximum)
mot_de_passe = "admin123"
tentatives = 0
acces = False
while tentatives < 3:
    saisie = input("Entrez le mot de passe : ")
    if saisie == mot_de_passe:
        print("Accès autorisé.")
        acces = True
        break
    else:
        tentatives += 1
        restantes = 3 - tentatives
        print(f"Mot de passe incorrect. Tentatives restantes : {restantes}")

if not acces:
    print("Accès bloqué : trop de tentatives incorrectes.")


# Exercice 13 — Surveillance de l’utilisation CPU
cpu = 95
while cpu > 80:
    print(f"Alerte : CPU à {cpu} %")
    cpu -= 5
print(f"CPU revenu à un niveau acceptable : {cpu} %")


# Exercice 14 — Lecture continue des logs système
logs = ["INFO", "INFO", "WARNING", "INFO", "ERREUR", "INFO"]
for message in logs:
    if message == "ERREUR":
        print("ERREUR détectée — arrêt de la lecture.")
        break
    print(f"Log lu : {message}")


# Exercice 15 — Vérification d’espace disque
espace = 20  # Go disponibles au départ
while espace < 50:
    print(f"Nettoyage en cours... Espace actuel : {espace} Go")
    espace += 5
print(f"Nettoyage terminé. Espace libre final : {espace} Go")