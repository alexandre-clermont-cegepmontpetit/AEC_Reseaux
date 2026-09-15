<#
.SYNOPSIS
    Crée en lot des comptes utilisateurs Active Directory à partir d'un fichier CSV.

.DESCRIPTION
    Le script lit un fichier CSV (séparé par des points-virgules) contenant le nom,
    le prénom, le poste et le statut d'administrateur de chaque personne à créer, puis
    crée les comptes correspondants dans l'unité d'organisation "Utilisateurs" située
    à la racine du domaine.

    - Le nom de compte est formé de la 1re lettre du prénom et des 4 premières du nom.
    - Le mot de passe est formé des 2 premières lettres du nom en majuscules, des
      2 premières lettres du prénom en minuscules et d'un nombre aléatoire de 4 chiffres.
    - Les personnes marquées "Oui" dans la colonne Admin sont ajoutées au groupe des
      admins du domaine.

    Chaque action est journalisée dans %LOCALAPPDATA%\Import-ADUsers.log et le script
    retourne sur le pipeline un objet par compte créé.

.PARAMETER Path
    Chemin (absolu ou relatif) du fichier CSV à importer. Le fichier doit exister.

.EXAMPLE
    .\Import-ADUsers.ps1 -Path ".\users.csv"

    Compte MotDePasse Admin
    ------ ---------- -----
    basse  ASbe5678   False
    agent  GEal1998    True

.NOTES
    Auteur    : Prénom Nom                <<< À REMPLACER
    Matricule : 1234567                   <<< À REMPLACER
    Cours     : Administration de systèmes
    Travail   : TP2 - Création de comptes AD en lot
    Date      : 2026-08-25
#>

#Requires -Modules ActiveDirectory

[CmdletBinding(SupportsShouldProcess = $true)]
Param (
    # Chemin du fichier CSV. Obligatoire, et validé par PowerShell lui-même:
    # le script plante avant même de démarrer si le fichier n'existe pas.
    [Parameter(Mandatory = $true)]
    [ValidateScript({ Test-Path -Path $_ -PathType Leaf })]
    [String]
    $Path
)

#region Fonctions

function Write-Log {
    <#
    .SYNOPSIS
        Consigne un message horodaté dans le journal du script.

    .DESCRIPTION
        La fonction est responsable de construire l'horodatage (format ISO 8601),
        de déterminer l'emplacement du journal dans le profil de l'utilisateur
        courant à l'aide d'une variable d'environnement Windows, et de créer le
        fichier s'il n'existe pas encore.

    .PARAMETER Message
        Le texte à consigner dans le journal.

    .EXAMPLE
        Write-Log -Message "=== Début du script ==="
    #>
    [CmdletBinding()]
    Param (
        [Parameter(Mandatory = $true)]
        [String]
        $Message
    )

    # Le chemin n'est jamais codé en dur: il est construit à partir de la variable
    # d'environnement LOCALAPPDATA (C:\Users\<utilisateur>\AppData\Local).
    $FichierJournal = Join-Path -Path $env:LOCALAPPDATA -ChildPath "Import-ADUsers.log"

    # Création du fichier au besoin. Out-Null empêche l'objet retourné par New-Item
    # de se retrouver sur le pipeline de sortie du script.
    if (-not (Test-Path -Path $FichierJournal -PathType Leaf)) {
        New-Item -Path $FichierJournal -ItemType "File" -Force | Out-Null
    }

    # Format "o" (aller-retour .NET) = ISO 8601 complet avec décalage horaire,
    # par exemple 2026-08-25T15:29:35.9082949-04:00
    $Horodatage = Get-Date -Format "o"

    Add-Content -Path $FichierJournal -Value "$Horodatage`t$Message"
}

#endregion Fonctions

#region Programme principal

Write-Log -Message "=== Début du script ==="

# On interroge Active Directory plutôt que de coder le domaine en dur: le script
# fonctionne ainsi dans n'importe quel domaine, sans modification.
$Domaine = Get-ADDomain
$UnitedOrganisation = "OU=Utilisateurs,$($Domaine.DistinguishedName)"

# Le groupe des admins du domaine est repéré par son SID (RID 512) plutôt que par son
# nom, qui change selon la langue du système ("Admins du domaine" / "Domain Admins").
$GroupeAdmins = Get-ADGroup -Identity "$($Domaine.DomainSID.Value)-512"

# Importation du fichier reçu en paramètre. Le CSV est séparé par des points-virgules.
$Personnes = Import-Csv -Path $Path -Delimiter ";"

foreach ($Personne in $Personnes) {

    Write-Log -Message "Traitement de l'utilisateur $($Personne.Prenom) $($Personne.Nom) ($($Personne.Poste))"

    # Nom de compte: 1re lettre du prénom + 4 premières lettres du nom, en minuscules.
    $NomDeCompte = ($Personne.Prenom.Substring(0, 1) + $Personne.Nom.Substring(0, 4)).ToLower()

    # Mot de passe: 2 lettres du nom en MAJUSCULES + 2 lettres du prénom en minuscules
    # + 4 chiffres aléatoires. Le paramètre -Maximum étant exclusif, 10000 donne 1000-9999.
    $NombreAleatoire = Get-Random -Minimum 1000 -Maximum 10000
    $MotDePasse = $Personne.Nom.Substring(0, 2).ToUpper() +
                  $Personne.Prenom.Substring(0, 2).ToLower() +
                  $NombreAleatoire

    # La colonne Admin du CSV contient "Oui" ou "Non": on la convertit en booléen.
    $EstAdmin = $Personne.Admin -eq "Oui"

    # Les paramètres de création du compte sont regroupés dans une table de hachage
    # et passés à la commande par splatting.
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
        # Aucune erreur n'est affichée à l'écran: elle est consignée dans le journal.
        Write-Log -Message "ERREUR lors du traitement de $NomDeCompte : $($_.Exception.Message)"
    }
}

Write-Log -Message "=== Fin du script ==="

#endregion Programme principal
