<#
.SYNOPSIS
    Supprime les comptes créés par Import-ADUsers.ps1 (utilitaire de test, non remis).

.DESCRIPTION
    Relit le même fichier CSV, recalcule les noms de compte selon la même règle et
    supprime les comptes correspondants s'ils existent. Permet de relancer le TP
    autant de fois que nécessaire pendant le développement.

.EXAMPLE
    .\Remove-ADUsersTest.ps1 -Path ".\users.csv"
#>

#Requires -Modules ActiveDirectory

[CmdletBinding(SupportsShouldProcess = $true)]
Param (
    [Parameter(Mandatory = $true)]
    [ValidateScript({ Test-Path -Path $_ -PathType Leaf })]
    [String]
    $Path
)

$Personnes = Import-Csv -Path $Path -Delimiter ";"

foreach ($Personne in $Personnes) {

    $NomDeCompte = ($Personne.Prenom.Substring(0, 1) + $Personne.Nom.Substring(0, 4)).ToLower()

    $Compte = Get-ADUser -Filter "SamAccountName -eq '$NomDeCompte'"

    if ($null -ne $Compte) {
        Remove-ADUser -Identity $Compte -Confirm:$false
        Write-Host -Object "Compte $NomDeCompte supprimé."
    }
    else {
        Write-Host -Object "Compte $NomDeCompte introuvable."
    }
}
