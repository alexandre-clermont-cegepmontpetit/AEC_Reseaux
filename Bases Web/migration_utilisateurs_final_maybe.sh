#!/bin/bash

###########################################################################
# VARIABLES
###########################################################################

IP_TFTP="192.168.0.15"
BD="TP2-BD.txt"
BD_LOCALE="$HOME/$BD"
TOTAL_REPERTOIRES=0

###########################################################################
# FONCTIONS
###########################################################################

# Télécharger le fichier de configuration depuis le serveur TFTP
telecharger_config() {
    busybox tftp -g -r "$BD" "$IP_TFTP" -l "$BD_LOCALE"
    if [ $? -ne 0 ]; then
        echo "Erreur: Échec du téléchargement de $BD depuis le serveur TFTP"
        exit 1
    fi
}

# Créer le répertoire home de l'utilisateur
creer_repertoire_home() {
    local repertoire_home=$1
    mkdir -p "$repertoire_home"
    if [ $? -ne 0 ]; then
        echo "Erreur: Échec de la création du répertoire home $repertoire_home"
        return 1
    fi
    return 0
}

# Créer les répertoires standards
creer_repertoires_standards() {
    local repertoire_home=$1
    local repertoires=("Documents" "Projects" "Media" "Downloads")
    
    for repertoire in "${repertoires[@]}"; do
        mkdir -p "$repertoire_home/$repertoire"
        if [ $? -ne 0 ]; then
            echo "Erreur: Échec de la création de $repertoire dans $repertoire_home"
            return 1
        fi
        ((TOTAL_REPERTOIRES++))
    done
    return 0
}

# Définir les permissions
definir_permissions() {
    local repertoire_home=$1
    chmod -R 750 "$repertoire_home"
    if [ $? -ne 0 ]; then
        echo "Erreur: Échec de la définition des permissions pour $repertoire_home"
        return 1
    fi
    return 0
}

# Afficher les informations du répertoire
afficher_info_repertoire() {
    local repertoire_home=$1
    local nom_utilisateur=$2
    
    # Obtenir la taille du répertoire
    local taille=$(du -sh "$repertoire_home" | cut -f1)
    echo "La taille du répertoire $repertoire_home est $taille"
    
    # Compter les répertoires
    local nombre_repertoires=$(find "$repertoire_home" -mindepth 1 -maxdepth 1 -type d | wc -l)
    echo "Nombre de répertoires dans $repertoire_home: $nombre_repertoires"
    
    return 0
}

# Traiter une ligne d'utilisateur
traiter_ligne_utilisateur() {
    local ligne="$1"
    local nom_utilisateur mot_passe uid gid repertoire_home shell
    IFS=':' read -r nom_utilisateur mot_passe uid gid _ repertoire_home shell <<< "$ligne"
    
    # Créer un groupe avec le nom d'utilisateur
    groupadd "$nom_utilisateur"
    
    # Assigner un groupe secondaire basé sur le nombre d'utilisateurs
    ((compteur_utilisateurs++))
    case $((compteur_utilisateurs % 4)) in
        1) groupe_secondaire="groupe1"; groupadd "$groupe_secondaire" 2>/dev/null ;;
        2) groupe_secondaire="groupe2"; groupadd "$groupe_secondaire" 2>/dev/null ;;
        3) groupe_secondaire="groupe3"; groupadd "$groupe_secondaire" 2>/dev/null ;;
        0) groupe_secondaire="groupe4"; groupadd "$groupe_secondaire" 2>/dev/null ;;
    esac
    
    # Créer l'utilisateur
    useradd -g "$nom_utilisateur" -G "$groupe_secondaire" -d "$repertoire_home" -s "$shell" "$nom_utilisateur"
    echo "$nom_utilisateur:$mot_passe" | chpasswd
    if [ $? -ne 0 ]; then
        echo "Erreur: Échec de la création de l'utilisateur $nom_utilisateur"
        return
    fi
    
    # Créer le répertoire home
    creer_repertoire_home "$repertoire_home"
    
    # Créer les répertoires standards
    creer_repertoires_standards "$repertoire_home"
    
    # Définir les permissions
    definir_permissions "$repertoire_home"
    
    # Créer le fichier .bash_aliases
    cat > "$repertoire_home/.bash_aliases" << EOF
alias update='apt update'
alias upgrade='apt upgrade'
alias user='whoami'
alias ipa='hostname -I'
EOF
    
    # Définir la propriété du répertoire home et de son contenu
    chown -R "$nom_utilisateur:$nom_utilisateur" "$repertoire_home"
    
    # Afficher les informations du répertoire
    afficher_info_repertoire "$repertoire_home" "$nom_utilisateur"
}

###########################################################################
# CODE PRINCIPAL
###########################################################################

main() {
    # Télécharger le fichier de configuration
    telecharger_config
    
    # Vérifier si le fichier de configuration existe
    if [ ! -f "$BD_LOCALE" ]; then
        echo "Erreur: Fichier de configuration $BD_LOCALE introuvable"
        exit 1
    fi
    
    # Compteur pour les utilisateurs
    local compteur_utilisateurs=0
    
    # Lire le fichier de configuration ligne par ligne
    while IFS= read -r ligne || [ -n "$ligne" ]; do
        traiter_ligne_utilisateur "$ligne"
    done < "$BD_LOCALE"
    
    # Afficher les statistiques finales
    echo "Nombre total de répertoires créés: $TOTAL_REPERTOIRES"
    echo "Nombre total d'utilisateurs créés: $compteur_utilisateurs"
}

# Exécuter la fonction principale ("main" par convention)
main
