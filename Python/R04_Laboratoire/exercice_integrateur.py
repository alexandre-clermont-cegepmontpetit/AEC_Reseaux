# Exercice intégrateur — Gestion interactive d'équipements réseau

# Liste vide pour stocker les équipements (dictionnaires)
equipements = []

# Constantes pour la plage de VLANs autorisée
VLAN_MIN = 10
VLAN_MAX = 100


def ajouter_equipement():
    """Demande les informations à l'utilisateur et ajoute l'équipement à la liste."""
    hostname = input("Hostname (ex. R1) : ")
    ip = input("Adresse IP (ex. 192.168.1.1) : ")
    os = input("Système d'exploitation (ex. Cisco IOS) : ")

    # Saisie des VLANs séparés par des virgules
    saisie_vlans = input("VLANs séparés par des virgules (ex. 10, 20, 30) : ")

    # Transformer les VLANs en liste d'entiers et valider la plage
    vlans = []
    for valeur in saisie_vlans.split(","):
        valeur = valeur.strip()
        if valeur == "":
            continue
        vlan = int(valeur)
        if VLAN_MIN <= vlan <= VLAN_MAX:
            vlans.append(vlan)
            print("VLAN", vlan, ": ✅ autorisé")
        else:
            print("VLAN", vlan, ": ❌ hors plage autorisée (non ajouté)")

    # Convertir le champ admin en booléen
    saisie_admin = input("Administrable à distance (oui/non) : ")
    admin = saisie_admin.strip().lower() == "oui"

    # Créer le dictionnaire de l'équipement
    equipement = {
        "hostname": hostname,
        "ip": ip,
        "os": os,
        "vlans": vlans,
        "admin": admin
    }

    # Ajouter à la liste
    equipements.append(equipement)
    print("Équipement ajouté avec succès !\n")


def afficher_equipements():
    """Affiche tous les équipements enregistrés."""
    if len(equipements) == 0:
        print("Aucun équipement enregistré.\n")
        return

    print("\nListe des équipements :")
    for eq in equipements:
        print(eq)
    print()


# Boucle principale du menu interactif
while True:
    print("===== Gestion des équipements réseau =====")
    print("1. Ajouter un équipement")
    print("2. Afficher tous les équipements")
    print("3. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_equipement()
    elif choix == "2":
        afficher_equipements()
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.\n")
