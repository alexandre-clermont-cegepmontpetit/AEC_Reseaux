/* =====================================================================
   MINI-PROJET : GESTION D'UNE ÉCOLE DE FORMATION CONTINUE
   ---------------------------------------------------------------------
   SCRIPT 03 - Vues, procédure stockée et requêtes de vérification
   ---------------------------------------------------------------------
   À exécuter après les scripts 01 et 02.
   Ces objets préparent la partie 3 (site web ASP.NET) :
     - les VUES alimentent les pages « Liste des inscriptions »,
       « Liste des professeurs », « Liste des cours »... ;
     - la PROCÉDURE sert au bouton « S'inscrire » du formulaire.
   Vous pouvez exécuter tout le script (F5) ou une requête à la fois
   (sélectionnez-la avec la souris, puis F5).
   ===================================================================== */

USE GestionEcole;
GO

/* =====================================================================
   PARTIE A - LES VUES
   Une vue = une requête SELECT enregistrée sous un nom.
   On l'utilise ensuite comme une table :  SELECT * FROM dbo.vw_...
   (CREATE OR ALTER : crée la vue, ou la remplace si elle existe déjà)
   ===================================================================== */

-- Vue 1 : liste complète des inscriptions (page « Liste des inscriptions »)
CREATE OR ALTER VIEW dbo.vw_ListeInscriptions
AS
SELECT  i.Matricule,
        e.Prenom + N' ' + e.Nom     AS Etudiant,
        i.CodeCours,
        c.Description               AS Cours,
        p.NomProgramme              AS Programme,
        i.CodeSession,
        s.Libelle                   AS Session,
        s.DateDebut,
        s.DateFin,
        i.DateInscription,
        i.Note,
        pr.Prenom + N' ' + pr.Nom   AS ProfesseurPrincipal,
        c.CodeSalle                 AS Salle
FROM dbo.Inscription   AS i
JOIN dbo.Etudiant      AS e   ON e.Matricule      = i.Matricule
JOIN dbo.Cours         AS c   ON c.CodeCours      = i.CodeCours
JOIN dbo.Programme     AS p   ON p.CodeProgramme  = c.CodeProgramme
JOIN dbo.Session       AS s   ON s.CodeSession    = i.CodeSession
JOIN dbo.Professeur    AS pr  ON pr.NumProfesseur = c.NumProfesseur;
GO

-- Vue 2 : liste des professeurs + nombre de cours dont ils sont responsables
--         (LEFT JOIN : on garde aussi les professeurs qui n'ont aucun cours)
CREATE OR ALTER VIEW dbo.vw_ListeProfesseurs
AS
SELECT  pr.NumProfesseur,
        pr.Nom,
        pr.Prenom,
        pr.Telephone,
        pr.Adresse,
        COUNT(c.CodeCours) AS NbCoursPrincipal
FROM dbo.Professeur    AS pr
LEFT JOIN dbo.Cours    AS c  ON c.NumProfesseur = pr.NumProfesseur
GROUP BY pr.NumProfesseur, pr.Nom, pr.Prenom, pr.Telephone, pr.Adresse;
GO

-- Vue 3 : catalogue des cours (programme, professeur principal, salle)
CREATE OR ALTER VIEW dbo.vw_ListeCours
AS
SELECT  c.CodeCours,
        c.Description,
        p.NomProgramme              AS Programme,
        pr.Prenom + N' ' + pr.Nom   AS ProfesseurPrincipal,
        sa.CodeSalle,
        sa.Libelle                  AS Salle
FROM dbo.Cours         AS c
JOIN dbo.Programme     AS p   ON p.CodeProgramme  = c.CodeProgramme
JOIN dbo.Professeur    AS pr  ON pr.NumProfesseur = c.NumProfesseur
JOIN dbo.Salle         AS sa  ON sa.CodeSalle     = c.CodeSalle;
GO

-- Vue 4 : bulletin de notes avec le résultat (Réussite si note >= 60)
CREATE OR ALTER VIEW dbo.vw_Bulletin
AS
SELECT  i.Matricule,
        e.Prenom + N' ' + e.Nom     AS Etudiant,
        i.CodeSession,
        i.CodeCours,
        c.Description               AS Cours,
        i.Note,
        CASE
            WHEN i.Note IS NULL THEN N'En attente'
            WHEN i.Note >= 60   THEN N'Réussite'
            ELSE                     N'Échec'
        END                         AS Resultat
FROM dbo.Inscription   AS i
JOIN dbo.Etudiant      AS e  ON e.Matricule = i.Matricule
JOIN dbo.Cours         AS c  ON c.CodeCours = i.CodeCours;
GO

-- Vue 5 : statistiques par cours et par session (nombre d'inscrits, moyenne)
CREATE OR ALTER VIEW dbo.vw_StatistiquesCours
AS
SELECT  i.CodeSession,
        i.CodeCours,
        c.Description                       AS Cours,
        COUNT(*)                            AS NbInscrits,
        COUNT(i.Note)                       AS NbNotesSaisies,   -- COUNT(colonne) ignore les NULL
        CAST(AVG(i.Note) AS DECIMAL(5,2))   AS Moyenne           -- AVG ignore aussi les NULL
FROM dbo.Inscription   AS i
JOIN dbo.Cours         AS c  ON c.CodeCours = i.CodeCours
GROUP BY i.CodeSession, i.CodeCours, c.Description;
GO

/* =====================================================================
   PARTIE B - PROCÉDURE STOCKÉE pour le formulaire « Inscription »
   Le formulaire du gabarit demande : Prénom, Nom, Courriel, Téléphone,
   Sexe, Cours choisi et Date de début (= la session choisie).
     1) si le courriel existe déjà, on réutilise cet étudiant ;
     2) sinon on crée l'étudiant (SQL Server génère le matricule) ;
     3) on l'inscrit au cours pour la session choisie.
   ===================================================================== */
CREATE OR ALTER PROCEDURE dbo.ps_InscrireEtudiant
    @Prenom       NVARCHAR(50),
    @Nom          NVARCHAR(50),
    @Courriel     VARCHAR(100),
    @Telephone    VARCHAR(20),
    @Sexe         CHAR(1),
    @CodeCours    VARCHAR(10),
    @CodeSession  CHAR(5)
AS
BEGIN
    SET NOCOUNT ON;     -- n'affiche pas « 1 row(s) affected »
    SET XACT_ABORT ON;  -- en cas d'erreur, tout est annulé

    -- Règle : on ne peut pas s'inscrire à une session déjà terminée
    IF NOT EXISTS (SELECT 1
                   FROM dbo.Session
                   WHERE CodeSession = @CodeSession
                     AND DateFin >= CAST(GETDATE() AS DATE))
        THROW 50010, N'Cette session n''existe pas ou elle est déjà terminée.', 1;

    DECLARE @Matricule INT;

    BEGIN TRANSACTION;

    -- 1) L'étudiant existe-t-il déjà ? On le cherche par son courriel.
    SELECT @Matricule = Matricule
    FROM dbo.Etudiant
    WHERE Courriel = @Courriel;

    -- 2) Sinon, on le crée. SCOPE_IDENTITY() donne le matricule qui vient d'être généré.
    IF @Matricule IS NULL
    BEGIN
        INSERT INTO dbo.Etudiant (Nom, Prenom, Telephone, Courriel, Sexe)
        VALUES (@Nom, @Prenom, @Telephone, @Courriel, @Sexe);

        SET @Matricule = SCOPE_IDENTITY();
    END;

    -- 3) Règle : pas deux fois le même cours dans la même session
    IF EXISTS (SELECT 1
               FROM dbo.Inscription
               WHERE Matricule = @Matricule
                 AND CodeCours = @CodeCours
                 AND CodeSession = @CodeSession)
        THROW 50011, N'Cet étudiant est déjà inscrit à ce cours pour cette session.', 1;

    -- 4) L'inscription (DateInscription prend sa valeur par défaut : aujourd'hui)
    INSERT INTO dbo.Inscription (Matricule, CodeCours, CodeSession)
    VALUES (@Matricule, @CodeCours, @CodeSession);

    COMMIT TRANSACTION;

    -- Renvoie le matricule au site web (ex. : « Votre matricule est le 1013 »)
    SELECT @Matricule AS Matricule;
END;
GO

-- Test de la procédure : une nouvelle étudiante s'inscrit à ASP.NET débutant pour l'hiver 2027.
-- (Exécutez-la une 2e fois : vous verrez le message de la règle « déjà inscrit ».)
EXEC dbo.ps_InscrireEtudiant
     @Prenom      = N'Jade',
     @Nom         = N'Leclerc',
     @Courriel    = 'jade.leclerc@example.com',
     @Telephone   = '450-555-0123',
     @Sexe        = 'F',
     @CodeCours   = 'ASP-101',
     @CodeSession = 'H2027';
GO

/* =====================================================================
   PARTIE C - SAISIE D'UNE NOTE PAR LE PROFESSEUR
   (ce que fera la page « Saisie des notes » du site)
   ===================================================================== */
UPDATE dbo.Inscription
SET    Note = 85
WHERE  Matricule   = 1007
  AND  CodeCours   = 'ASP-101'
  AND  CodeSession = 'A2026';
GO

/* =====================================================================
   PARTIE D - REQUÊTES DE VÉRIFICATION
   (sélectionnez une requête puis F5 pour l'exécuter seule)
   ===================================================================== */

-- 1. Toutes les inscriptions, triées par session puis par étudiant
--    (une vue ne peut pas contenir ORDER BY : on trie ici)
SELECT *
FROM dbo.vw_ListeInscriptions
ORDER BY DateDebut, Etudiant;

-- 2. Liste des professeurs
SELECT *
FROM dbo.vw_ListeProfesseurs
ORDER BY Nom, Prenom;

-- 3. Catalogue des cours d'un programme
SELECT *
FROM dbo.vw_ListeCours
WHERE Programme = N'AEC Développement Web'
ORDER BY CodeCours;

-- 4. Les étudiants inscrits à « ASP.NET débutant » à l'automne 2026
SELECT Matricule, Etudiant, DateInscription
FROM dbo.vw_ListeInscriptions
WHERE CodeCours = 'ASP-101'
  AND CodeSession = 'A2026'
ORDER BY Etudiant;

-- 5. Nombre d'étudiants différents par programme (GROUP BY)
SELECT Programme,
       COUNT(DISTINCT Matricule) AS NbEtudiants
FROM dbo.vw_ListeInscriptions
GROUP BY Programme
ORDER BY NbEtudiants DESC;

-- 6. Bulletin d'un étudiant (Samuel Pelletier a repris ASP-101)
SELECT CodeSession, CodeCours, Cours, Note, Resultat
FROM dbo.vw_Bulletin
WHERE Matricule = 1003
ORDER BY CodeSession;

-- 7. Moyenne par cours et par session (uniquement là où des notes existent)
SELECT *
FROM dbo.vw_StatistiquesCours
WHERE NbNotesSaisies > 0
ORDER BY CodeSession, CodeCours;

-- 8. Les professeurs qui ne sont responsables d'aucun cours (LEFT JOIN ... IS NULL)
SELECT pr.NumProfesseur, pr.Prenom, pr.Nom
FROM dbo.Professeur AS pr
LEFT JOIN dbo.Cours AS c ON c.NumProfesseur = pr.NumProfesseur
WHERE c.CodeCours IS NULL;

-- 9. Les étudiants qui n'ont encore aucune inscription (NOT EXISTS)
SELECT e.Matricule, e.Prenom, e.Nom, e.Courriel
FROM dbo.Etudiant AS e
WHERE NOT EXISTS (SELECT 1
                  FROM dbo.Inscription AS i
                  WHERE i.Matricule = e.Matricule);

-- 10. Les cours donnés dans chaque salle
SELECT sa.CodeSalle, sa.Libelle, c.CodeCours, c.Description
FROM dbo.Salle AS sa
LEFT JOIN dbo.Cours AS c ON c.CodeSalle = sa.CodeSalle
ORDER BY sa.CodeSalle, c.CodeCours;
GO
