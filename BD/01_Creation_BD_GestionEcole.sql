/* =====================================================================
   MINI-PROJET : GESTION D'UNE ÉCOLE DE FORMATION CONTINUE
   ---------------------------------------------------------------------
   SCRIPT 01 - Création de la base de données (modèle relationnel)
     Étape 1 : suppression de l'ancienne base (si elle existe)
     Étape 2 : création de la base GestionEcole
     Étape 3 : création des tables avec leur CLÉ PRIMAIRE
     Étape 4 : création des CLÉS ÉTRANGÈRES
     Étape 5 : création des CONTRAINTES (UNIQUE, CHECK, DEFAULT)
     Étape 6 : création des INDEX
     Étape 7 : vérification
   ---------------------------------------------------------------------
   COMMENT L'EXÉCUTER DANS SSMS 22 :
     1. Fichier > Ouvrir > Fichier... et choisissez ce script.
     2. Appuyez sur F5 (ou cliquez sur « Execute »).
     3. Dans l'Explorateur d'objets : clic droit sur « Databases »
        > Refresh, pour voir apparaître la base GestionEcole.

   ATTENTION : ce script SUPPRIME puis RECRÉE la base GestionEcole.
   Vous pouvez donc le relancer autant de fois que vous voulez pour
   repartir à zéro (mais les données seront effacées : relancez
   ensuite le script 02).
   ===================================================================== */

USE master;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 1 : suppression de l'ancienne base (si elle existe déjà)
   --------------------------------------------------------------------- */
IF DB_ID(N'GestionEcole') IS NOT NULL
BEGIN
    -- Ferme les autres connexions ouvertes sur la base (sinon : « base en cours d'utilisation »)
    ALTER DATABASE GestionEcole SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE GestionEcole;
END;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 2 : création de la base de données
   (les fichiers .mdf et .ldf sont créés dans le dossier par défaut)
   --------------------------------------------------------------------- */
CREATE DATABASE GestionEcole;
GO

USE GestionEcole;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 3 : création des tables, chacune avec sa CLÉ PRIMAIRE (PK)
   Ordre : d'abord les tables « parents » (qui ne dépendent de personne),
   ensuite les tables qui les référencent.
   Types utilisés :
     NVARCHAR  = texte avec accents (noms, adresses...)
     VARCHAR   = texte simple sans accents (codes, courriel, téléphone)
     DATE      = une date (AAAA-MM-JJ)
     INT IDENTITY(début, pas) = numéro généré automatiquement
   --------------------------------------------------------------------- */

-- PROGRAMME : AEC Développement Web, AEC Sécurité, AEC Concepteur de BD...
CREATE TABLE dbo.Programme
(
    CodeProgramme  VARCHAR(10)    NOT NULL,   -- ex. : 'AEC-WEB'
    NomProgramme   NVARCHAR(100)  NOT NULL,   -- ex. : 'AEC Développement Web'
    CONSTRAINT PK_Programme PRIMARY KEY (CodeProgramme)
);

-- PROFESSEUR
CREATE TABLE dbo.Professeur
(
    NumProfesseur  INT IDENTITY(1,1) NOT NULL, -- généré automatiquement : 1, 2, 3...
    Nom            NVARCHAR(50)   NOT NULL,
    Prenom         NVARCHAR(50)   NOT NULL,
    Telephone      VARCHAR(20)    NOT NULL,
    Adresse        NVARCHAR(200)  NOT NULL,
    CONSTRAINT PK_Professeur PRIMARY KEY (NumProfesseur)
);

-- SALLE
CREATE TABLE dbo.Salle
(
    CodeSalle      VARCHAR(10)    NOT NULL,   -- ex. : 'B-204'
    Libelle        NVARCHAR(100)  NOT NULL,   -- ex. : 'Laboratoire informatique B-204'
    CONSTRAINT PK_Salle PRIMARY KEY (CodeSalle)
);

-- SESSION : période d'études avec une date de début et une date de fin
CREATE TABLE dbo.Session
(
    CodeSession    CHAR(5)        NOT NULL,   -- ex. : 'A2026' (A = automne, H = hiver, E = été)
    Libelle        NVARCHAR(50)   NOT NULL,   -- ex. : 'Automne 2026'
    DateDebut      DATE           NOT NULL,
    DateFin        DATE           NOT NULL,
    CONSTRAINT PK_Session PRIMARY KEY (CodeSession)
);

-- ETUDIANT
CREATE TABLE dbo.Etudiant
(
    Matricule      INT IDENTITY(1001,1) NOT NULL, -- généré automatiquement : 1001, 1002, 1003...
    Nom            NVARCHAR(50)   NOT NULL,
    Prenom         NVARCHAR(50)   NOT NULL,
    Adresse        NVARCHAR(200)  NULL,       -- NULL permis : le formulaire d'inscription du site ne la demande pas
    Telephone      VARCHAR(20)    NOT NULL,
    DateNaissance  DATE           NULL,       -- NULL permis : même raison (l'administration la complétera)
    Courriel       VARCHAR(100)   NOT NULL,   -- ajouté : demandé dans le formulaire d'inscription
    Sexe           CHAR(1)        NULL,       -- ajouté : 'F' = Femme, 'H' = Homme (formulaire d'inscription)
    CONSTRAINT PK_Etudiant PRIMARY KEY (Matricule)
);

-- COURS : chaque cours appartient à UN programme, a UN professeur principal
--         et se donne dans UNE salle  ->  3 clés étrangères (ajoutées à l'étape 4)
CREATE TABLE dbo.Cours
(
    CodeCours      VARCHAR(10)    NOT NULL,   -- ex. : 'ASP-101'
    Description    NVARCHAR(150)  NOT NULL,   -- ex. : 'ASP.NET débutant'
    CodeProgramme  VARCHAR(10)    NOT NULL,   -- programme dont fait partie le cours
    NumProfesseur  INT            NOT NULL,   -- professeur principal du cours
    CodeSalle      VARCHAR(10)    NOT NULL,   -- salle où le cours est donné
    CONSTRAINT PK_Cours PRIMARY KEY (CodeCours)
);

-- INSCRIPTION : table issue de l'association S'INSCRIRE du MCD
--   (un étudiant s'inscrit à un cours pendant une session).
--   Sa clé primaire est COMPOSÉE de 3 colonnes : un étudiant ne peut
--   donc pas s'inscrire deux fois au même cours dans la même session,
--   mais il peut reprendre le cours à une autre session.
CREATE TABLE dbo.Inscription
(
    Matricule        INT           NOT NULL,  -- quel étudiant
    CodeCours        VARCHAR(10)   NOT NULL,  -- à quel cours
    CodeSession      CHAR(5)       NOT NULL,  -- pendant quelle session
    DateInscription  DATE          NOT NULL,  -- par défaut : la date du jour (étape 5)
    Note             DECIMAL(5,2)  NULL,      -- note d'examen saisie par le professeur (NULL = pas encore saisie)
    CONSTRAINT PK_Inscription PRIMARY KEY (Matricule, CodeCours, CodeSession)
);
GO

/* ---------------------------------------------------------------------
   ÉTAPE 4 : création des CLÉS ÉTRANGÈRES (FK)
   Une clé étrangère garantit que la valeur existe dans la table parent.
   Exemple : impossible d'inscrire l'étudiant 9999 s'il n'existe pas.
   Par défaut, SQL Server refuse aussi de supprimer un parent qui a
   encore des « enfants » (ex. : un programme qui contient des cours).
   --------------------------------------------------------------------- */
ALTER TABLE dbo.Cours
    ADD CONSTRAINT FK_Cours_Programme
        FOREIGN KEY (CodeProgramme) REFERENCES dbo.Programme (CodeProgramme);

ALTER TABLE dbo.Cours
    ADD CONSTRAINT FK_Cours_Professeur
        FOREIGN KEY (NumProfesseur) REFERENCES dbo.Professeur (NumProfesseur);

ALTER TABLE dbo.Cours
    ADD CONSTRAINT FK_Cours_Salle
        FOREIGN KEY (CodeSalle) REFERENCES dbo.Salle (CodeSalle);

ALTER TABLE dbo.Inscription
    ADD CONSTRAINT FK_Inscription_Etudiant
        FOREIGN KEY (Matricule) REFERENCES dbo.Etudiant (Matricule);

ALTER TABLE dbo.Inscription
    ADD CONSTRAINT FK_Inscription_Cours
        FOREIGN KEY (CodeCours) REFERENCES dbo.Cours (CodeCours);

ALTER TABLE dbo.Inscription
    ADD CONSTRAINT FK_Inscription_Session
        FOREIGN KEY (CodeSession) REFERENCES dbo.Session (CodeSession);
GO

/* ---------------------------------------------------------------------
   ÉTAPE 5 : création des CONTRAINTES (règles de gestion)
     UNIQUE  = pas de doublon dans la colonne
     CHECK   = la valeur doit respecter une condition
     DEFAULT = valeur utilisée si on n'en donne pas
   --------------------------------------------------------------------- */

-- Règle : deux programmes ne peuvent pas porter le même nom
ALTER TABLE dbo.Programme
    ADD CONSTRAINT UQ_Programme_Nom UNIQUE (NomProgramme);

-- Règle : code de session = A (automne), H (hiver) ou E (été) suivi de l'année
ALTER TABLE dbo.Session
    ADD CONSTRAINT CK_Session_Code CHECK (CodeSession LIKE '[AHE][0-9][0-9][0-9][0-9]');

-- Règle : une session se termine après avoir commencé
ALTER TABLE dbo.Session
    ADD CONSTRAINT CK_Session_Dates CHECK (DateFin > DateDebut);

-- Règle : deux étudiants ne peuvent pas avoir le même courriel
ALTER TABLE dbo.Etudiant
    ADD CONSTRAINT UQ_Etudiant_Courriel UNIQUE (Courriel);

-- Règle : le courriel doit avoir la forme  texte@texte.texte
ALTER TABLE dbo.Etudiant
    ADD CONSTRAINT CK_Etudiant_Courriel CHECK (Courriel LIKE '%_@_%._%');

-- Règle : le sexe vaut 'F' ou 'H' (boutons Femme / Homme du formulaire)
ALTER TABLE dbo.Etudiant
    ADD CONSTRAINT CK_Etudiant_Sexe CHECK (Sexe IN ('F', 'H'));

-- Règle : la date de naissance est dans le passé
ALTER TABLE dbo.Etudiant
    ADD CONSTRAINT CK_Etudiant_DateNaissance CHECK (DateNaissance < CAST(GETDATE() AS DATE));

-- Règle : une note est comprise entre 0 et 100
ALTER TABLE dbo.Inscription
    ADD CONSTRAINT CK_Inscription_Note CHECK (Note BETWEEN 0 AND 100);

-- Valeur par défaut : si on ne précise pas la date d'inscription, c'est aujourd'hui
ALTER TABLE dbo.Inscription
    ADD CONSTRAINT DF_Inscription_DateInscription
        DEFAULT (CAST(GETDATE() AS DATE)) FOR DateInscription;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 6 : création des INDEX
   SQL Server crée AUTOMATIQUEMENT un index pour chaque PRIMARY KEY
   et chaque contrainte UNIQUE. Par contre, il n'en crée PAS pour les
   clés étrangères : on les ajoute nous-mêmes pour accélérer les
   jointures (JOIN) utilisées par les listes du site web.
   --------------------------------------------------------------------- */
CREATE NONCLUSTERED INDEX IX_Cours_CodeProgramme     ON dbo.Cours (CodeProgramme);
CREATE NONCLUSTERED INDEX IX_Cours_NumProfesseur     ON dbo.Cours (NumProfesseur);
CREATE NONCLUSTERED INDEX IX_Cours_CodeSalle         ON dbo.Cours (CodeSalle);
CREATE NONCLUSTERED INDEX IX_Inscription_CodeCours   ON dbo.Inscription (CodeCours);
CREATE NONCLUSTERED INDEX IX_Inscription_CodeSession ON dbo.Inscription (CodeSession);
-- (Inscription.Matricule est la 1re colonne de la clé primaire : il est déjà indexé)

-- Recherche rapide d'une personne par son nom (champ « Rechercher » du site)
CREATE NONCLUSTERED INDEX IX_Etudiant_Nom_Prenom     ON dbo.Etudiant (Nom, Prenom);
CREATE NONCLUSTERED INDEX IX_Professeur_Nom_Prenom   ON dbo.Professeur (Nom, Prenom);
GO

/* ---------------------------------------------------------------------
   ÉTAPE 7 : vérification (résultats dans l'onglet « Results »)
   --------------------------------------------------------------------- */
-- Les 7 tables créées
SELECT name AS TableCreee
FROM sys.tables
ORDER BY name;

-- Toutes les contraintes : PK, FK, UNIQUE, CHECK et DEFAULT
SELECT OBJECT_NAME(parent_object_id) AS NomTable,
       name                          AS NomContrainte,
       type_desc                     AS TypeContrainte
FROM sys.objects
WHERE type IN ('PK', 'F', 'UQ', 'C', 'D')
ORDER BY NomTable, TypeContrainte;

-- Tous les index
SELECT OBJECT_NAME(i.object_id) AS NomTable,
       i.name                   AS NomIndex,
       i.type_desc              AS TypeIndex,
       i.is_unique              AS EstUnique
FROM sys.indexes AS i
JOIN sys.tables  AS t ON t.object_id = i.object_id
WHERE i.name IS NOT NULL
ORDER BY NomTable, NomIndex;

PRINT N'Script 01 terminé : base GestionEcole créée. Exécutez maintenant le script 02.';
GO
