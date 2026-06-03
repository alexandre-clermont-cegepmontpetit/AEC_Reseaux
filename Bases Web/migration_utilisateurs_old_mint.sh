#!/bin/bash

###########################################################################
# VARIABLES
###########################################################################
IP_SERVEUR_TFTP="192.168.0.15"
FICHIER_TFTP="TP2-BD.txt"
FICHIER_LOCAL="$HOME/TP2-BD.txt"
GROUPE_SECONDAIRE_COMPTEUR=1
TOTAL_REPERTOIRES=0
TOTAL_UTILISATEURS_CREES=0

###########################################################################
# TMP: SUPPRIMER QUAND TERMINÉ
###########################################################################
echo "###########################################################################"
echo "# SCRIPT COMMENCE ICI"
echo "###########################################################################"
echo "IP_SERVEUR_TFTP = $IP_SERVEUR_TFTP"
echo "FICHIER_TFTP = $FICHIER_TFTP"
echo "FICHIER_LOCAL = $FICHIER_LOCAL"
echo "GROUPE_SECONDAIRE_COMPTEUR = $GROUPE_SECONDAIRE_COMPTEUR"
echo "TOTAL_REPERTOIRES = $TOTAL_REPERTOIRES"
echo "TOTAL_UTILISATEURS_CREES = $TOTAL_UTILISATEURS_CREES"

###########################################################################
# FONCTIONS
###########################################################################

# Fonction pour télécharger le fichier depuis le serveur TFTP
telecharger_fichier() {
    echo "[INFO] Téléchargement du fichier depuis TFTP..."
    busybox tftp -g -r "$FICHIER_TFTP" "$IP_SERVEUR_TFTP" -l "$FICHIER_LOCAL"
    if [ $? -ne 0 ]; then
        echo "[ERREUR] Échec du téléchargement du fichier TFTP."
        exit 1
    fi
    echo "[OK] Fichier téléchargé : $FICHIER_LOCAL"
}

# Fonction pour créer le répertoire principal
creer_repertoire_principal() {
    local home_dir="$1"
    mkdir -p "$home_dir"
    chown "$username:$username" "$home_dir"
}

# Fonction pour créer les sous-répertoires
creer_sous_repertoires() {
    local home_dir="$1"
    for dir in Documents Projects Media Downloads; do
        mkdir -p "$home_dir/$dir"
        chown "$username:$username" "$home_dir/$dir"
    done
}

# Fonction pour initialiser le fichier .bash_aliases
initialiser_aliases() {
    local home_dir="$1"
    cat <<EOF > "$home_dir/.bash_aliases"
alias update='apt update'
alias upgrade='apt upgrade'
alias user='whoami'
alias ipa='hostname -I'
EOF
    chown "$username:$username" "$home_dir/.bash_aliases"
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

    # Créer le groupe secondaire selon le compteur
    groupe_secondaire="groupe$GROUPE_SECONDAIRE_COMPTEUR"
    if ! getent group "$groupe_secondaire" > /dev/null; then
        groupadd "$groupe_secondaire"
    fi

    # Créer le groupe principal (même nom que l'utilisateur)
    if ! getent group "$username" > /dev/null; then
        groupadd -g "$gid" "$username"
    fi

    # Créer l’utilisateur
    useradd -u "$uid" -g "$gid" -G "$groupe_secondaire" -d "$home" -s "$shell" "$username"
    echo "$username:$password" | chpasswd

    # Initialisation de l’environnement
    creer_repertoire_principal "$home"
    creer_sous_repertoires "$home"
    initialiser_aliases "$home"
    ajuster_permissions "$home"
    afficher_infos "$home"

    TOTAL_UTILISATEURS_CREES=$((TOTAL_UTILISATEURS_CREES + 1))
    GROUPE_SECONDAIRE_COMPTEUR=$((GROUPE_SECONDAIRE_COMPTEUR % 4 + 1))

done < "$FICHIER_LOCAL"

rm -f "$FICHIER_LOCAL"

echo "---------------------------------------------"
echo "Nombre total d'utilisateurs créés : $TOTAL_UTILISATEURS_CREES"
echo "Nombre total de répertoires créés : $TOTAL_REPERTOIRES"
echo "---------------------------------------------"
