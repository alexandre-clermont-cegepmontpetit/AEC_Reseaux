/* =====================================================================
   MINI-PROJET : GESTION D'UNE ÉCOLE DE FORMATION CONTINUE
   ---------------------------------------------------------------------
   SCRIPT 02 - Insertion des données de test
   ---------------------------------------------------------------------
   À exécuter JUSTE APRÈS le script 01 (base neuve et vide).

   Ordre des insertions : on remplit d'abord les tables « parents »,
   puis les tables qui les référencent (sinon les clés étrangères
   refusent les lignes) :
     Programme -> Salle -> Session -> Professeur -> Cours
     -> Etudiant -> Inscription

   Tout est dans UNE transaction : si une seule ligne est refusée,
   RIEN n'est inséré. En cas d'erreur : corrigez, puis relancez le
   script 01 et ce script 02 (dans cet ordre).

   Rappels :
   - le préfixe N devant un texte (N'Émilie') conserve les accents ;
   - une apostrophe dans un texte s'écrit en double : N'l''école' ;
   - les dates s'écrivent 'AAAA-MM-JJ'.
   ===================================================================== */

USE GestionEcole;
GO

SET XACT_ABORT ON;   -- à la moindre erreur : annulation complète

-- Sécurité : si les données sont déjà là, on arrête tout de suite
IF EXISTS (SELECT 1 FROM dbo.Programme)
    THROW 50001, N'Les données sont déjà insérées. Pour tout recommencer : exécutez le script 01, puis ce script 02.', 1;

BEGIN TRANSACTION;

/* 1. PROGRAMMES ------------------------------------------------------ */
INSERT INTO dbo.Programme (CodeProgramme, NomProgramme)
VALUES
    ('AEC-WEB', N'AEC Développement Web'),
    ('AEC-SEC', N'AEC Sécurité informatique'),
    ('AEC-BD',  N'AEC Concepteur de bases de données');

/* 2. SALLES ---------------------------------------------------------- */
INSERT INTO dbo.Salle (CodeSalle, Libelle)
VALUES
    ('A-101', N'Salle de classe A-101'),
    ('B-204', N'Laboratoire informatique B-204'),
    ('B-210', N'Laboratoire informatique B-210'),
    ('C-015', N'Laboratoire de réseautique C-015');

/* 3. SESSIONS -------------------------------------------------------- */
INSERT INTO dbo.Session (CodeSession, Libelle, DateDebut, DateFin)
VALUES
    ('H2026', N'Hiver 2026',   '2026-01-19', '2026-05-15'),
    ('E2026', N'Été 2026',     '2026-05-25', '2026-08-14'),
    ('A2026', N'Automne 2026', '2026-08-24', '2026-12-18'),
    ('H2027', N'Hiver 2027',   '2027-01-18', '2027-05-14');

/* 4. PROFESSEURS -----------------------------------------------------
   On NE donne PAS le numéro : SQL Server le génère (IDENTITY 1, 2, 3...).
   Le numéro obtenu est indiqué en commentaire à droite de chaque ligne. */
INSERT INTO dbo.Professeur (Nom, Prenom, Telephone, Adresse)
VALUES
    (N'Tremblay', N'Julie',   '514-555-0101', N'1200, rue Saint-Denis, Montréal'),          -- n° 1
    (N'Gagnon',   N'Marc',    '450-555-0102', N'45, boulevard Taschereau, Brossard'),       -- n° 2
    (N'Roy',      N'Sophie',  '450-555-0103', N'78, rue Victoria, Saint-Lambert'),          -- n° 3
    (N'Côté',     N'Karim',   '514-555-0104', N'350, avenue du Parc, Montréal'),            -- n° 4
    (N'Bouchard', N'Nadia',   '450-555-0105', N'910, chemin de Chambly, Longueuil'),        -- n° 5
    (N'Nguyen',   N'Olivier', '438-555-0106', N'58, rue Sherbrooke Est, Montréal');         -- n° 6 (aucun cours pour l'instant)

/* 5. COURS -----------------------------------------------------------
   Chaque cours : un programme, un professeur principal (n°) et une salle.
   Les 3 cours ASP.NET sont ceux affichés sur la page d'accueil du gabarit. */
INSERT INTO dbo.Cours (CodeCours, Description, CodeProgramme, NumProfesseur, CodeSalle)
VALUES
    ('ASP-101', N'ASP.NET débutant',                          'AEC-WEB', 1, 'B-204'),
    ('ASP-201', N'ASP.NET intermédiaire',                     'AEC-WEB', 1, 'B-204'),
    ('ASP-301', N'ASP.NET avancé',                            'AEC-WEB', 2, 'B-210'),
    ('WEB-110', N'HTML5 et CSS3',                             'AEC-WEB', 2, 'A-101'),
    ('SEC-101', N'Introduction à la sécurité informatique',   'AEC-SEC', 3, 'C-015'),
    ('SEC-201', N'Sécurité des réseaux',                      'AEC-SEC', 3, 'C-015'),
    ('BD-101',  N'Introduction aux bases de données',         'AEC-BD',  4, 'B-210'),
    ('BD-201',  N'Modélisation des données (Merise)',         'AEC-BD',  4, 'A-101'),
    ('BD-301',  N'Administration de SQL Server',              'AEC-BD',  5, 'B-210');

/* 6. ÉTUDIANTS -------------------------------------------------------
   On NE donne PAS le matricule : SQL Server le génère (IDENTITY 1001, 1002...).
   Le matricule obtenu est indiqué en commentaire à droite de chaque ligne.
   Girard et Petit se sont inscrits par le site web : pas encore d'adresse
   ni de date de naissance (NULL). */
INSERT INTO dbo.Etudiant (Nom, Prenom, Adresse, Telephone, DateNaissance, Courriel, Sexe)
VALUES
    (N'Lavoie',    N'Émilie',    N'12, rue Principale, Laval',            '514-555-0111', '1998-03-14', 'emilie.lavoie@example.com',    'F'), -- 1001
    (N'Diallo',    N'Mamadou',   N'88, boulevard Cousineau, Longueuil',   '450-555-0112', '1995-11-02', 'mamadou.diallo@example.com',   'H'), -- 1002
    (N'Pelletier', N'Samuel',    N'5, rue des Érables, Boucherville',     '450-555-0113', '2000-07-21', 'samuel.pelletier@example.com', 'H'), -- 1003
    (N'Nguyen',    N'Linh',      N'230, rue Jarry Ouest, Montréal',       '514-555-0114', '1997-01-30', 'linh.nguyen@example.com',      'F'), -- 1004
    (N'Morin',     N'Catherine', N'17, rue Green, Saint-Lambert',         '450-555-0115', '1990-09-09', 'catherine.morin@example.com',  'F'), -- 1005
    (N'Haddad',    N'Youssef',   N'402, rue Beaubien Est, Montréal',      '514-555-0116', '1993-05-17', 'youssef.haddad@example.com',   'H'), -- 1006
    (N'Gauthier',  N'Alexandre', N'64, rue Saint-Charles, Longueuil',     '450-555-0117', '1999-12-05', 'alex.gauthier@example.com',    'H'), -- 1007
    (N'Fortin',    N'Chloé',     N'9, place Charles-Le Moyne, Longueuil', '438-555-0118', '2001-04-25', 'chloe.fortin@example.com',     'F'), -- 1008
    (N'Ouellet',   N'Mathieu',   N'150, boulevard Taschereau, Brossard',  '450-555-0119', '1988-08-08', 'mathieu.ouellet@example.com',  'H'), -- 1009
    (N'Benali',    N'Sarah',     N'33, avenue Victoria, Saint-Lambert',   '514-555-0120', '1996-02-11', 'sarah.benali@example.com',     'F'), -- 1010
    (N'Girard',    N'Félix',     NULL,                                     '450-555-0121', NULL,         'felix.girard@example.com',     'H'), -- 1011
    (N'Petit',     N'Léa',       NULL,                                     '438-555-0122', NULL,         'lea.petit@example.com',        'F'); -- 1012 (aucune inscription)

/* 7. INSCRIPTIONS ----------------------------------------------------
   (Matricule, CodeCours, CodeSession, DateInscription, Note)
   - sessions terminées (H2026, E2026) : la note est saisie ;
   - session en cours (A2026) et future (H2027) : note = NULL.
   Remarque : Samuel Pelletier (1003) a échoué ASP-101 à l'hiver 2026
   et le reprend à l'été 2026 -> c'est possible grâce à la session
   dans la clé primaire. */
INSERT INTO dbo.Inscription (Matricule, CodeCours, CodeSession, DateInscription, Note)
VALUES
    -- Hiver 2026
    (1001, 'ASP-101', 'H2026', '2026-01-05', 88.00),
    (1002, 'ASP-101', 'H2026', '2026-01-06', 72.50),
    (1003, 'ASP-101', 'H2026', '2026-01-08', 55.00),
    (1004, 'BD-101',  'H2026', '2026-01-07', 91.00),
    (1005, 'BD-101',  'H2026', '2026-01-10', 67.00),
    (1006, 'SEC-101', 'H2026', '2026-01-09', 79.00),
    (1009, 'WEB-110', 'H2026', '2026-01-12', 84.00),
    -- Été 2026
    (1003, 'ASP-101', 'E2026', '2026-05-11', 74.00),
    (1007, 'WEB-110', 'E2026', '2026-05-12', 81.00),
    (1010, 'BD-201',  'E2026', '2026-05-15', 93.00),
    -- Automne 2026 (session en cours)
    (1001, 'ASP-201', 'A2026', '2026-08-10', NULL),
    (1002, 'ASP-201', 'A2026', '2026-08-11', NULL),
    (1004, 'BD-201',  'A2026', '2026-08-12', NULL),
    (1005, 'BD-201',  'A2026', '2026-08-12', NULL),
    (1006, 'SEC-201', 'A2026', '2026-08-14', NULL),
    (1007, 'ASP-101', 'A2026', '2026-08-15', NULL),
    (1008, 'ASP-101', 'A2026', '2026-08-18', NULL),
    (1009, 'SEC-101', 'A2026', '2026-08-19', NULL),
    (1010, 'BD-301',  'A2026', '2026-08-20', NULL),
    (1011, 'ASP-101', 'A2026', '2026-08-21', NULL),
    -- Hiver 2027 (inscriptions à l'avance)
    (1001, 'ASP-301', 'H2027', '2026-09-15', NULL),
    (1004, 'BD-301',  'H2027', '2026-09-16', NULL),
    (1008, 'ASP-201', 'H2027', '2026-09-18', NULL);

COMMIT TRANSACTION;

PRINT N'Script 02 terminé : données insérées avec succès.';
GO

/* ---------------------------------------------------------------------
   VÉRIFICATION : nombre de lignes par table
   Résultat attendu : Programme 3, Salle 4, Session 4, Professeur 6,
                      Cours 9, Etudiant 12, Inscription 23
   --------------------------------------------------------------------- */
SELECT 'Programme'   AS NomTable, COUNT(*) AS NbLignes FROM dbo.Programme
UNION ALL SELECT 'Salle',       COUNT(*) FROM dbo.Salle
UNION ALL SELECT 'Session',     COUNT(*) FROM dbo.Session
UNION ALL SELECT 'Professeur',  COUNT(*) FROM dbo.Professeur
UNION ALL SELECT 'Cours',       COUNT(*) FROM dbo.Cours
UNION ALL SELECT 'Etudiant',    COUNT(*) FROM dbo.Etudiant
UNION ALL SELECT 'Inscription', COUNT(*) FROM dbo.Inscription;

-- Les matricules générés automatiquement
SELECT Matricule, Prenom, Nom, Courriel
FROM dbo.Etudiant
ORDER BY Matricule;
GO

/* ---------------------------------------------------------------------
   BONUS : testez vos contraintes !
   Pour chaque ligne ci-dessous : enlevez les deux tirets -- du début,
   sélectionnez la ligne, puis F5. SQL Server doit la REFUSER
   (message rouge dans l'onglet « Messages ») : c'est normal, c'est
   la preuve que la contrainte fonctionne.
   --------------------------------------------------------------------- */
-- INSERT INTO dbo.Inscription (Matricule, CodeCours, CodeSession) VALUES (9999, 'ASP-101', 'A2026');   -- FK : l'étudiant 9999 n'existe pas
-- INSERT INTO dbo.Inscription (Matricule, CodeCours, CodeSession) VALUES (1001, 'ASP-201', 'A2026');   -- PK : déjà inscrit à ce cours pour cette session
-- UPDATE dbo.Inscription SET Note = 120 WHERE Matricule = 1001 AND CodeCours = 'ASP-101';              -- CHECK : une note ne dépasse pas 100
-- INSERT INTO dbo.Session (CodeSession, Libelle, DateDebut, DateFin) VALUES ('E2027', N'Été 2027', '2027-06-10', '2027-06-01'); -- CHECK : la fin est avant le début
-- INSERT INTO dbo.Etudiant (Nom, Prenom, Telephone, Courriel) VALUES (N'Test', N'Test', '514-555-0199', 'lea.petit@example.com'); -- UNIQUE : courriel déjà utilisé
-- DELETE FROM dbo.Programme WHERE CodeProgramme = 'AEC-WEB';                                           -- FK : ce programme contient encore des cours
