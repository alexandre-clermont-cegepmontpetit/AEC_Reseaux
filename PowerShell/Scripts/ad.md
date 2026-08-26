# Commandes PowerShell Active Directory

<span style="color:green">Pour visionner : `Ctrl + Shift + V`</span>

Voici les commandes PowerShell exactes telles qu'elles sont écrites dans "6 - Active Directory.pdf", organisées selon leur contexte dans les diapositives :

### Installation et modules
*   **Installer le module RSAT AD PowerShell sur Windows Server :**
    `Install-WindowsFeature -Name "RSAT-AD-PowerShell"`
*   **Installer les outils RSAT ADDS sur Windows Server :**
    `Install-WindowsFeature -Name "RSAT-ADDS"`
*   **Installer la console de gestion des stratégies de groupe (GPMC) sur Windows Server :**
    `Install-WindowsFeature -Name "GPMC"`
*   **Installer les outils RSAT AD en ligne pour Windows 10 :**
    `Add-WindowsCapability -Online -Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"`
*   **Installer RSAT GPMC en ligne pour Windows 10 :**
    `Add-WindowsCapability -Online -Name "Rsat.GroupPolicy.Management.Tools~~~~0.0.1.0"`
*   **Importer le module Active Directory dans la session :**
    `Import-Module -Name "ActiveDirectory"`
*   **Lister toutes les commandes disponibles dans le module Active Directory :**
    `Get-Command -Module "ActiveDirectory"`
*   **Installer le module communautaire ADSIPS :**
    `Install-Module -Name ADSIPS -Scope CurrentUser`
*   **Importer le module communautaire ADSIPS :**
    `Import-Module -Name ADSIPS`

### Lecture des informations AD
*   **Obtenir les informations du domaine :**
    `Get-ADDomain`
*   **Obtenir les informations de la forêt :**
    `Get-ADForest`
*   **Lire les unités d'organisation (OU) :**
    `Get-ADOrganizationalUnit`
*   **Lire les comptes utilisateurs :**
    `Get-ADUser`
*   **Lire les comptes ordinateurs :**
    `Get-ADComputer`
*   **Lire les groupes AD :**
    `Get-ADGroup`
*   **Lire les membres d'un groupe AD :**
    `Get-ADGroupMember`
*   **Trouver le DN racine (Root DN) du domaine :**
    `Get-ADRootDSE`
*   **Lire les informations d'un utilisateur à l'aide du module ADSIPS :**
    `Get-ADSIUser -Identity "laboratoire\vincent.carrier"`

### Requêtes sur les utilisateurs avec filtres et propriétés
*   **Obtenir un utilisateur et exposer la propriété LastLogonTimestamp :**
    `Get-ADUser -Identity "yvon.bosse" -Properties "LastLogonTimestamp"`
*   **Stocker un objet utilisateur dans une variable et afficher son horodatage :**
    `$user = Get-ADUser -Identity "yvon.bosse" -Properties "LastLogonTimestamp"`
    `$user.LastLogonTimestamp`
*   **Convertir le format de temps brut d'AD en une date et heure lisibles (DateTime) :**
    `[datetime]::fromFileTimeUTC($user.LastLogonTimestamp)`
*   **Filtrer les utilisateurs par SamAccountName commençant par "A" :**
    `Get-ADUser -Filter { SamAccountName -like "A*" }`
*   **Rechercher les utilisateurs dont le nom commence par "A" dans une OU spécifique :**
    `$SearchBase = "OU=LABINFO,DC=labinfo,DC=local"`
    `Get-ADUser -Filter { Name -like "A*" } -SearchBase $SearchBase`
*   **Construire une base de recherche dynamique à l'aide du DefaultNamingContext :**
    `$DefaultNamingContext = Get-ADRootDSE | Select-Object -ExpandProperty "DefaultNamingContext"`
    `$UsersDN = "OU=Utilisateurs,$DefaultNamingContext"`
    `Get-ADUser -SearchBase $UsersDN -Filter * | Select-Object Name, SAMAccountName, SID, Enabled | Format-Table`

### Modification et suppression d'objets
*   **Ajouter plusieurs membres à un groupe spécifié :**
    `$Group = "Gestionnaires"`
    `$Members = "Bob", "Eric"`
    `Add-ADGroupMember -Identity $Group -Members $Members`
*   **Mettre à jour l'adresse courriel d'un utilisateur à l'aide de variables :**
    `$Identity = "Bob"`
    `$EmailAddress = "bob@cegepmontpetit.ca"`
    `Set-ADUser -Identity $Identity -EmailAddress $EmailAddress`
*   **Mettre à jour l'adresse courriel d'un utilisateur à l'aide du pipeline :**
    `Get-ADUser -Identity "Bob" | Set-ADUser -EmailAddress $EmailAddress`
*   **Stocker un utilisateur dans une variable et le transmettre via le pipeline pour le supprimer :**
    `$User = Get-ADUser -Identity "Eric"`
    `$User | Remove-ADUser`
*   **Supprimer un utilisateur en ignorant l'invite de confirmation :**
    `Remove-ADUser -Confirm:$False`

### Création d'objets et mots de passe
*   **Créer une nouvelle unité d'organisation :**
    `New-ADOrganizationalUnit`
*   **Créer un nouveau compte utilisateur :**
    `New-ADUser`
*   **Créer un nouveau compte ordinateur :**
    `New-ADComputer`
*   **Créer un nouveau groupe :**
    `New-ADGroup`
*   **Convertir une chaîne de texte brut en une chaîne sécurisée (secure string) :**
    `$Motdepasse = ConvertTo-SecureString "Password!" -AsPlainText -Force`
*   **Demander à la console de saisir une chaîne sécurisée :**
    `$Motdepasse = Read-Host "Entrez un mot de passe" -AsSecureString`
*   **Créer un utilisateur via la technique du "splatting" :**
    ```powershell
    $ADUserSplat = @{
        Path = "OU=Users,OU=LABINFO,DC=labinfo,DC=local"
        Name = "Zoe Zappa" 
        GivenName = "Zoe" 
        Surname = "Zappa" 
        Initials = "Z."
        Title = "Dr."
        DisplayName = "Dr. Zoe Zappa" 
        Description = "VP de chépokoi"
        SamAccountName = "zzappa"
        UserPrincipalName = "zzappa@labinfo.local"
        AccountPassword = ("Password!" | ConvertTo-SecureString -AsPlainText -Force)
        ChangePasswordAtLogon = $true
        Manager = (Get-ADUser -Identity "Daniel")
        StreetAddress = "42 rue des cannes de bouffe à chat"
        City = "Minoupolis"
        Country = "CA"
        PostalCode = "C4L 1S5"
        MobilePhone = "(555) 555-5555"
        EmployeeNumber = "1002735"
        EmailAddress = "zzappa@labinfo.com"
        Enabled = $true
    }
    New-ADUser @ADUserSplat -Verbose
    ```
