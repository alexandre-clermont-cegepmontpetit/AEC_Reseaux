#!/bin/bash

###########################################################################
# VARIABLES
###########################################################################
IP_SERVEUR_TFTP="192.168.0.15"
BD_TFTP="TP2-BD.txt"
BD_LOCALE="$HOME/TP2-BD.txt"
COMPTEUR_GROUPES_SECONDAIRES=1
TOTAL_REPERTOIRES=0
TOTAL_UTILISATEURS_CREES=0

###########################################################################
# TMP: SUPPRIMER QUAND TERMINÉ
###########################################################################
echo "###########################################################################"
echo "# SCRIPT COMMENCE ICI"
echo "###########################################################################"
echo "IP_SERVEUR_TFTP = $IP_SERVEUR_TFTP"
echo "BD_TFTP = $BD_TFTP"
echo "BD_LOCALE = $BD_LOCALE"
echo "COMPTEUR_GROUPES_SECONDAIRES = $COMPTEUR_GROUPES_SECONDAIRES"
echo "TOTAL_REPERTOIRES = $TOTAL_REPERTOIRES"
echo "TOTAL_UTILISATEURS_CREES = $TOTAL_UTILISATEURS_CREES"

###########################################################################
# FONCTIONS
###########################################################################

# Fonction pour télécharger le fichier depuis le serveur TFTP
telecharger_fichier() {
    echo "[INFO] Téléchargement du fichier depuis TFTP..."
    busybox tftp -g -r "$BD_TFTP" "$IP_SERVEUR_TFTP" -l "$BD_LOCALE"
    if [ $? -ne 0 ]; then
        echo "[ERREUR] Échec du téléchargement du fichier TFTP."
        exit 1
    fi
    echo "[OK] Fichier téléchargé : $BD_LOCALE"
}

# Fonction pour créer le répertoire principal
creer_repertoire_principal() {
    local home_dir="$1"
    local user="$2"
    mkdir -p "$home_dir"

    if getent group "$user" > /dev/null; then
        chown "$user:$user" "$home_dir"
    else
        echo "[WARN] Le groupe principal '$user' est introuvable. Affectation du propriétaire uniquement."
        chown "$user" "$home_dir"
    fi
}

# Fonction pour créer les sous-répertoires
creer_sous_repertoires() {
    local home_dir="$1"
    local user="$2"
    for dir in Documents Projects Media Downloads; do
        mkdir -p "$home_dir/$dir"

        if getent group "$user" > /dev/null; then
            chown "$user:$user" "$home_dir/$dir"
        else
            echo "[WARN] Le groupe principal '$user' est introuvable. Affectation du propriétaire uniquement."
            chown "$user" "$home_dir/$dir"
        fi
    done
}

# Fonction pour initialiser le fichier .bash_aliases
initialiser_aliases() {
    local home_dir="$1"
    local user="$2"
    cat <<EOF > "$home_dir/.bash_aliases"
alias update='apt update'
alias upgrade='apt upgrade'
alias user='whoami'
alias ipa='hostname -I'
EOF

    if getent group "$user" > /dev/null; then
        chown "$user:$user" "$home_dir/.bash_aliases"
    else
        echo "[WARN] Le groupe principal '$user' est introuvable. Affectation du propriétaire uniquement."
        chown "$user" "$home_dir/.bash_aliases"
    fi
}

# Fonction pour ajuster les permissions
ajuster_permissions() {
    local home_dir="$1"
    chmod 750 "$home_dir"
    chmod -R 750 "$home_dir"/*
}

# Fonction pour afficher les informations
afficher_infos() {
    local home_dir="$1"
    local taille
    local nb_repertoires

    taille=$(du -sh "$home_dir" | cut -f1)
    nb_repertoires=$(find "$home_dir" -mindepth 1 -maxdepth 1 -type d | wc -l)

    echo "La taille du répertoire $home_dir est $taille"
    echo "Le nombre de répertoires dans $home_dir est $nb_repertoires"

    TOTAL_REPERTOIRES=$((TOTAL_REPERTOIRES + nb_repertoires))
}

###########################################################################
# CODE PRINCIPAL
###########################################################################

# Étape 1 : Télécharger la base de données
telecharger_fichier

# Étape 2 : Lire le fichier et créer les comptes
while IFS=: read -r username password uid gid comment home shell; do
    echo "[INFO] Création de l'utilisateur : $username"

    # Si UID déjà utilisé, ignorer entièrement ce compte
    if getent passwd "$uid" > /dev/null; then
        echo "[WARN] UID '$uid' déjà utilisé. Utilisateur ignoré."
        continue
    fi

    utilisateur_cree=false

    # Créer le groupe secondaire selon le compteur
    groupe_secondaire="groupe$COMPTEUR_GROUPES_SECONDAIRES"
    if ! getent group "$groupe_secondaire" > /dev/null; then
        groupadd "$groupe_secondaire"
    fi

    # Créer le groupe principal (même nom que l'utilisateur) si nécessaire
    if ! getent group "$username" > /dev/null; then
        echo "[INFO] Le groupe '$username' n'existe pas. Tentative de création."
        groupadd "$username"
    else
        echo "[INFO] Le groupe '$username' existe déjà."
    fi

    # Créer l’utilisateur si le nom n'existe pas (l’UID a déjà été filtré plus haut)
    if ! id "$username" &>/dev/null; then
        useradd -u "$uid" -g "$gid" -G "$groupe_secondaire" -d "$home" -s "$shell" "$username"
    
        if [ $? -eq 0 ]; then
            echo "$username:$password" | chpasswd
            if [ $? -ne 0 ]; then
                echo "[ERREUR] Impossible de définir le mot de passe pour $username"
            fi

            utilisateur_cree=true
            TOTAL_UTILISATEURS_CREES=$((TOTAL_UTILISATEURS_CREES + 1))
        else
            echo "[ERREUR] Échec de création de l'utilisateur $username"
        fi
    else
        echo "[WARN] Utilisateur '$username' existe déjà. Aucune action."
    fi

    # Initialisation de l’environnement
    if [ "$utilisateur_cree" = true ]; then
        creer_repertoire_principal "$home" "$username"
        creer_sous_repertoires "$home" "$username"
        initialiser_aliases "$home" "$username"
        ajuster_permissions "$home"
        afficher_infos "$home"
    else
        echo "[INFO] L'utilisateur '$username' ou son groupe principal est manquant. Environnement non initialisé."
    fi

    COMPTEUR_GROUPES_SECONDAIRES=$((COMPTEUR_GROUPES_SECONDAIRES % 4 + 1))

done < "$BD_LOCALE"

# Nettoyage
rm -f "$BD_LOCALE"

# Résumé
echo "---------------------------------------------"
echo "Nombre total d'utilisateurs créés : $TOTAL_UTILISATEURS_CREES"
echo "Nombre total de répertoires créés : $TOTAL_REPERTOIRES"
echo "---------------------------------------------"
