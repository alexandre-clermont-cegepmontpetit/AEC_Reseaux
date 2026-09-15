# CE SCRIPT CRÉE EN LOT DES COMPTES UTILISATEURS ACTIVE DIRECTORY À PARTIR D'UN FICHIER CSV
# PAR ALEXANDRE CLERMONT (MATRICULE: 0859542)

# Rend obligatoire et valide le chemin du fichier d'entrée.
[CmdletBinding(SupportsShouldProcess = $true)] # Active -WhatIf.
Param (
    # Chemin du fichier CSV (obligatoire et validé).
    [Parameter(Mandatory = $true)]
    [ValidateScript({ Test-Path -Path $_ -PathType Leaf })]
    [String] $Path
)

function Write-Log {
    # Écrit un message horodaté dans le journal du script.
    [CmdletBinding()]
    Param (
        [Parameter(Mandatory = $true)]
        [String] $Message
    )

    # Chemin du journal construit à partir de LOCALAPPDATA plutôt que codé en dur.
    $FichierJournal = Join-Path -Path $env:LOCALAPPDATA -ChildPath "Import-ADUsers.log"

    # Création du fichier au besoin. Out-Null empêche l'objet retourné par New-Item de se retrouver en sortie.
    if (-not (Test-Path -Path $FichierJournal -PathType Leaf)) {
        New-Item -Path $FichierJournal -ItemType "File" -Force | Out-Null
    }

    # Exemple de format "o" (ISO 8601): 2026-08-25T15:29:35.9082949-04:00.
    $Horodatage = Get-Date -Format "o"

    Add-Content -Path $FichierJournal -Value "$Horodatage`t$Message"
}

# PROGRAMME PRINCIPAL
Write-Log -Message "=== Début du script ==="

$Domaine = Get-ADDomain
$UnitedOrganisation = "OU=Utilisateurs,$($Domaine.DistinguishedName)"

# Le groupe des admins du domaine est repéré par son SID (RID 512).
$GroupeAdmins = Get-ADGroup -Identity "$($Domaine.DomainSID.Value)-512"

# Importation du fichier CSV reçu en paramètre.
$Personnes = Import-Csv -Path $Path -Delimiter ";"

foreach ($Personne in $Personnes) {

    Write-Log -Message "Traitement de l'utilisateur $($Personne.Prenom) $($Personne.Nom) ($($Personne.Poste))"

    # Nom de compte: première lettre du prénom + 4 premières lettres du nom (minuscules).
    $NomDeCompte = ($Personne.Prenom.Substring(0, 1) + $Personne.Nom.Substring(0, 4)).ToLower()

    # Mot de passe: 2 lettres du nom (majuscules)) + 2 lettres du prénom (minuscules) + 4 chiffres aléatoires.
    $NombreAleatoire = Get-Random -Minimum 1000 -Maximum 10000
    $MotDePasse = $Personne.Nom.Substring(0, 2).ToUpper() +
                  $Personne.Prenom.Substring(0, 2).ToLower() +
                  $NombreAleatoire

    # Conversion en booléen de colonne Admin du CSV (Oui/Non devient True/False).
    $EstAdmin = $Personne.Admin -eq "Oui"

    # Les paramètres de création du compte sont regroupés en hashtable et passés à la commande par splatting.
    $NouveauCompteSplat = @{
        Path                  = $UnitedOrganisation
        Name                  = $NomDeCompte
        SamAccountName        = $NomDeCompte
        UserPrincipalName     = $NomDeCompte
        GivenName             = $Personne.Prenom
        Surname               = $Personne.Nom
        DisplayName           = "$($Personne.Prenom) $($Personne.Nom)"
        Description           = $Personne.Poste
        AccountPassword       = (ConvertTo-SecureString -String $MotDePasse -AsPlainText -Force)
        ChangePasswordAtLogon = $true
        Enabled               = $true
    }

    try {
        New-ADUser @NouveauCompteSplat -ErrorAction Stop
        Write-Log -Message "Création de l'utilisateur $NomDeCompte complétée avec le mot de passe $MotDePasse"

        if ($EstAdmin) {
            Add-ADGroupMember -Identity $GroupeAdmins -Members $NomDeCompte -ErrorAction Stop
            Write-Log -Message "L'utilisateur $NomDeCompte a été défini comme admin du domaine"
        }

        # Seuls objets envoyés sur le pipeline de sortie du script.
        [PSCustomObject]@{
            Compte     = $NomDeCompte
            MotDePasse = $MotDePasse
            Admin      = $EstAdmin
        }
    }
    catch {
        # Aucune erreur affichée à l'écran (elle est plutôt écrite dans le journal).
        Write-Log -Message "ERREUR lors du traitement de $NomDeCompte : $($_.Exception.Message)"
    }
}

Write-Log -Message "=== Fin du script ==="