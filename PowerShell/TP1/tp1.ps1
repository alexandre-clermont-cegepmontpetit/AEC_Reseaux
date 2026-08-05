########################################################################################################################
# 420-B63-RO Scriptage sous Windows avec PowerShell
#
# Travail pratique #1 (Automne 2025)
#
# Noms de la personne étudiante:
#   - Nom, Prénom (Matricule)
#
########################################################################################################################


########################################################################################################################
### QUESTION 1 (10 points)
###



# a) Générez un rapport, sous forme de tableau, de tous les adapteurs réseau installés sur l'ordinateur, avec trois 
#    colonnees: le **nom de l’adapteur**, son **état** (connecté ou non) et son **adresse MAC**. *(2 points)*

Get-NetAdapter | Format-Table Name, Status, MacAddress



# b) Obtenez **le nombre** d’adapteurs réseau installés sur votre machine (et seulement le nombre). *(2 points)*

(Get-NetAdapter).Count

# (Variante équivalente: Get-NetAdapter | Measure-Object | Select-Object -ExpandProperty Count)



# c) Obtenez la liste des adapteurs qui sont connectés seulement. (2 points)

Get-NetAdapter | Where-Object Status -eq "Up"



# d) Obtenez la liste des adapteurs physiques (qui ne sont pas virtuels). (2 points)

Get-NetAdapter -Physical

# (Variante équivalente: Get-NetAdapter | Where-Object Virtual -eq $false)



# e) Obtenez la liste des adapteurs dont l’adresse MAC commence par 00-50. (2 points)

Get-NetAdapter | Where-Object MacAddress -like "00-50*"




########################################################################################################################
### QUESTION 2 (10 points)
###


# a) Chargez le contenu du fichier CSV et affectez-le à une variable. (2 point)
#    Le séparateur du fichier est le point-virgule: sans -Delimiter ";", PowerShell croit qu'il n'y a qu'une
#    seule colonne nommée "ID;Nom;Espece;...". -Encoding UTF8 assure le bon affichage des accents (ex.: Pâtée).
#    Note: exécutez vos commandes à partir du dossier qui contient data.csv (Set-Location).

$data = Import-Csv .\data.csv -Delimiter ";" -Encoding UTF8


# b) Obtenez la liste des animaux qui sont nés en 2020, triés par ordre décroissant de date, affiché
#    en format tableau. (2 points)

$data | Where-Object DateDeNaissance -like "2020*" | Sort-Object DateDeNaissance -Descending | Format-Table

# (Format-Table est nécessaire: avec 6 propriétés, PowerShell afficherait une liste par défaut.)


# c) Obtenez la liste des poissons mangeurs de foin et affichez-la en format tableau. (2 points)

$data | Where-Object { $_.Espece -eq "Poisson" -and $_.Nourriture -eq "Foin" } | Format-Table


# d) Obtenez la liste des lapins qui pèsent plus de 30 kg et affichez-la en format tableau. Attention au type des 
#    données! (2 points)
#    Import-Csv retourne du texte: sans la conversion [double], "8.36" -gt 30 serait vrai (comparaison de chaînes).

$data | Where-Object { $_.Espece -eq "Lapin" -and [double]$_.PoidsEnKg -gt 30 } | Format-Table


# e) Obtenez le nom (et seulement le nom) du plus vieux hamster. (2 points)
#    Les parenthèses + .Nom retournent la valeur seule (une chaîne), sans l'entête de colonne.

($data | Where-Object Espece -eq "Hamster" | Sort-Object DateDeNaissance | Select-Object -First 1).Nom




########################################################################################################################
### QUESTION BONUS! (2 points)
### 
### Dans votre ordinateur, il y a plusieurs interfaces réseau qui ont une adresse IP. Pourtant, une seule est connectée 
### à Internet.
###

# Élaborez une ligne de commande PowerShell qui obtient l'adresse IPv4 de l'interface qui sert à naviguer sur Internet.
# La carte qui sort sur Internet est celle qui porte la route par défaut (0.0.0.0/0) ayant la plus petite métrique.
# Le sous-pipeline entre parenthèses fournit son ifIndex à Get-NetIPAddress.

(Get-NetIPAddress -AddressFamily IPv4 -InterfaceIndex (Get-NetRoute -DestinationPrefix "0.0.0.0/0" | Sort-Object RouteMetric | Select-Object -First 1).ifIndex).IPAddress

# (Si plusieurs routes par défaut existent, on peut départager avec la métrique effective:
#  Sort-Object { $_.RouteMetric + $_.InterfaceMetric } )