/* =====================================================================
   MINI-PROJET : GESTION D'UNE ÉCOLE DE FORMATION CONTINUE
   ---------------------------------------------------------------------
   SCRIPT 04 - Plan de sauvegarde (backup) et test de restauration
   ---------------------------------------------------------------------
   LE PLAN
   +----------------+---------------------------+----------------------------------+
   | Type           | Quand                     | Contenu                          |
   +----------------+---------------------------+----------------------------------+
   | COMPLÈTE       | dimanche 23 h             | toute la base                    |
   | DIFFÉRENTIELLE | lundi à samedi 23 h       | ce qui a changé depuis la        |
   |                |                           | dernière complète                |
   | JOURNAL (LOG)  | toutes les heures,        | chaque transaction (inscription, |
   |                | de 8 h à 22 h             | note...) depuis le dernier LOG   |
   +----------------+---------------------------+----------------------------------+
   - Perte de données maximale : 1 heure (l'intervalle entre deux LOG).
   - Conservation : 4 semaines, puis on supprime les vieux fichiers.
   - Règle 3-2-1 : 3 copies, sur 2 supports différents, dont 1 hors
     du serveur (disque externe, OneDrive, Teams...).
   - Test de restauration : une fois par mois (étape 6 de ce script).
   - Pour restaurer : la COMPLÈTE, puis la dernière DIFFÉRENTIELLE,
     puis tous les JOURNAUX qui suivent, dans l'ordre.

   CE SCRIPT (à exécuter après 01 et 02, en entier avec F5) :
     1. passe la base en mode de récupération FULL ;
     2 à 4. fait une sauvegarde de chaque type ;
     5. vérifie les fichiers et affiche l'historique ;
     6. simule un incident (suppression par erreur) puis RESTAURE.

   Les fichiers sont écrits dans le dossier « Backup » par défaut de
   SQL Server (on ne donne que le nom du fichier, pas le chemin :
   ça évite les erreurs de permission « Access is denied »).
   ===================================================================== */

USE master;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 1 : mode de récupération FULL
   (obligatoire pour pouvoir sauvegarder le journal des transactions)
   --------------------------------------------------------------------- */
ALTER DATABASE GestionEcole SET RECOVERY FULL;
GO

-- Où les fichiers seront-ils créés ? Et quelle édition de SQL Server avez-vous ?
SELECT SERVERPROPERTY('InstanceDefaultBackupPath') AS DossierDesSauvegardes,
       SERVERPROPERTY('Edition')                   AS EditionSQLServer;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 2 : sauvegarde COMPLÈTE (le point de départ de tout le plan)
     INIT     = remplace l'ancien contenu du fichier
     CHECKSUM = vérifie chaque page pendant la sauvegarde
     STATS    = affiche la progression (25 %, 50 %...)
   --------------------------------------------------------------------- */
BACKUP DATABASE GestionEcole
    TO DISK = N'GestionEcole_COMPLETE.bak'
    WITH INIT, CHECKSUM, STATS = 25,
         NAME = N'GestionEcole - sauvegarde complète';
GO

/* ---------------------------------------------------------------------
   ÉTAPE 3 : la journée avance (un professeur saisit une note)...
             puis sauvegarde DIFFÉRENTIELLE
   --------------------------------------------------------------------- */
UPDATE GestionEcole.dbo.Inscription
SET    Note = 77
WHERE  Matricule = 1008 AND CodeCours = 'ASP-101' AND CodeSession = 'A2026';
GO

BACKUP DATABASE GestionEcole
    TO DISK = N'GestionEcole_DIFFERENTIELLE.bak'
    WITH DIFFERENTIAL, INIT, CHECKSUM, STATS = 25,
         NAME = N'GestionEcole - sauvegarde différentielle';
GO

/* ---------------------------------------------------------------------
   ÉTAPE 4 : encore du travail (une autre note)...
             puis sauvegarde du JOURNAL des transactions
   --------------------------------------------------------------------- */
UPDATE GestionEcole.dbo.Inscription
SET    Note = 83
WHERE  Matricule = 1011 AND CodeCours = 'ASP-101' AND CodeSession = 'A2026';
GO

BACKUP LOG GestionEcole
    TO DISK = N'GestionEcole_JOURNAL.trn'
    WITH INIT, CHECKSUM, STATS = 25,
         NAME = N'GestionEcole - sauvegarde du journal';
GO

/* ---------------------------------------------------------------------
   ÉTAPE 5 : vérifier que les sauvegardes sont lisibles
   (message attendu : « The backup set on file 1 is valid. »)
   --------------------------------------------------------------------- */
RESTORE VERIFYONLY FROM DISK = N'GestionEcole_COMPLETE.bak'       WITH CHECKSUM;
RESTORE VERIFYONLY FROM DISK = N'GestionEcole_DIFFERENTIELLE.bak' WITH CHECKSUM;
RESTORE VERIFYONLY FROM DISK = N'GestionEcole_JOURNAL.trn'        WITH CHECKSUM;
GO

-- Historique des sauvegardes (SQL Server le conserve dans la base système msdb)
SELECT TOP (10)
       bs.backup_finish_date AS DateSauvegarde,
       CASE bs.type
            WHEN 'D' THEN N'Complète'
            WHEN 'I' THEN N'Différentielle'
            WHEN 'L' THEN N'Journal'
       END                     AS TypeSauvegarde,
       bmf.physical_device_name AS Fichier
FROM msdb.dbo.backupset          AS bs
JOIN msdb.dbo.backupmediafamily  AS bmf ON bmf.media_set_id = bs.media_set_id
WHERE bs.database_name = N'GestionEcole'
ORDER BY bs.backup_finish_date DESC;
GO

/* ---------------------------------------------------------------------
   ÉTAPE 6 : TEST DE RESTAURATION (simulation d'un incident)
   Oups ! Quelqu'un efface TOUTES les inscriptions par erreur...
   --------------------------------------------------------------------- */
DELETE FROM GestionEcole.dbo.Inscription;

SELECT COUNT(*) AS InscriptionsApresIncident   -- résultat : 0
FROM GestionEcole.dbo.Inscription;
GO

-- On restaure dans l'ordre : COMPLÈTE -> DIFFÉRENTIELLE -> JOURNAL
--   NORECOVERY = « attends, il reste des sauvegardes à appliquer »
--   RECOVERY   = « c'est la dernière : rends la base utilisable »
--   REPLACE    = accepte d'écraser la base existante
USE master;

ALTER DATABASE GestionEcole SET SINGLE_USER WITH ROLLBACK IMMEDIATE;  -- déconnecte les autres fenêtres

RESTORE DATABASE GestionEcole FROM DISK = N'GestionEcole_COMPLETE.bak'       WITH REPLACE, NORECOVERY;
RESTORE DATABASE GestionEcole FROM DISK = N'GestionEcole_DIFFERENTIELLE.bak' WITH NORECOVERY;
RESTORE LOG      GestionEcole FROM DISK = N'GestionEcole_JOURNAL.trn'        WITH RECOVERY;

ALTER DATABASE GestionEcole SET MULTI_USER;
GO

-- Vérification : les inscriptions sont revenues (24 si vous avez exécuté le script 03,
-- sinon 23), et les notes 77 et 83 saisies avant l'incident n'ont pas été perdues.
SELECT COUNT(*) AS InscriptionsApresRestauration
FROM GestionEcole.dbo.Inscription;

SELECT Matricule, CodeCours, CodeSession, Note
FROM GestionEcole.dbo.Inscription
WHERE CodeCours = 'ASP-101' AND CodeSession = 'A2026'
ORDER BY Matricule;
GO

/* =====================================================================
   AUTOMATISER LE PLAN (à faire une seule fois)

   A) SQL Server Developer, Standard ou Enterprise (avec SQL Server Agent)
      Dans SSMS : Explorateur d'objets > Management > Maintenance Plans
      > clic droit > Maintenance Plan Wizard :
        - choisissez « Separate schedules for each task » ;
        - cochez Back Up Database (Full), Back Up Database (Differential),
          Back Up Database (Transaction Log) et Maintenance Cleanup Task ;
        - pour chaque tâche : base GestionEcole + l'horaire du plan
          (dimanche 23 h / lundi-samedi 23 h / toutes les heures) ;
        - Maintenance Cleanup Task : supprimer les fichiers .bak et .trn
          de plus de 4 semaines.
      (SQL Server Agent doit être démarré : clic droit > Start.)

   B) SQL Server Express (pas de SQL Server Agent)
      On utilise le Planificateur de tâches de Windows qui lance sqlcmd.
      1. Enregistrez le bloc ci-dessous dans C:\Scripts\Sauvegarde_Complete.sql
         (un nom de fichier différent chaque jour grâce à la date) :

         DECLARE @Fichier NVARCHAR(260) =
             N'GestionEcole_COMPLETE_' + FORMAT(SYSDATETIME(), 'yyyyMMdd_HHmm') + N'.bak';
         BACKUP DATABASE GestionEcole TO DISK = @Fichier WITH CHECKSUM, INIT;

      2. Planificateur de tâches > Créer une tâche de base > Hebdomadaire,
         dimanche 23 h > Démarrer un programme :
            Programme : sqlcmd
            Arguments : -S .\SQLEXPRESS -E -C -b -i "C:\Scripts\Sauvegarde_Complete.sql"
      3. Même principe pour la différentielle (WITH DIFFERENTIAL) et le
         journal (BACKUP LOG ... fichier .trn).
      4. Sans Agent, il n'y a pas de Maintenance Cleanup Task : supprimez
         vous-même les fichiers de plus de 4 semaines dans le dossier Backup.
      Si Windows répond que « sqlcmd » n'est pas reconnu, installez-le dans
      une invite de commandes avec :  winget install sqlcmd
   ===================================================================== */

/* =====================================================================
   EN CAS DE PROBLÈME PENDANT LA RESTAURATION
   - La base reste affichée « (Restoring...) » :
         RESTORE DATABASE GestionEcole WITH RECOVERY;
   - La base reste affichée « (Single User) » :
         ALTER DATABASE GestionEcole SET MULTI_USER;
   - Rien ne va plus : relancez les scripts 01 puis 02.
   ===================================================================== */
