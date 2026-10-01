using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Web.UI.WebControls;

// Liste des inscriptions (page d'administration).
// Lit la vue dbo.vw_ListeInscriptions, avec des filtres, le tri et la pagination,
// et calcule un résumé affiché dans la barre latérale.
// Le nom de la classe doit être le même que « Inherits » dans ListeInscriptions.aspx.
public partial class Pages_ListeInscriptions : System.Web.UI.Page
{
    const string CONNECTION_STRING = @"Data Source=localhost\COURS_BD;Initial Catalog=GestionEcole;Integrated Security=True;Encrypt=False;TrustServerCertificate=True;";

    // Requête sur la vue. Les @... sont des paramètres : la valeur tapée par
    // l'utilisateur n'est jamais collée dans le texte SQL (pas d'injection SQL).
    // Un paramètre NULL veut dire « pas de filtre ».
    // La colonne Resultat suit la règle de la vue vw_Bulletin (réussite à 60),
    // et signale en plus les notes oubliées dans une session déjà terminée.
    const string REQUETE_INSCRIPTIONS = @"
        SELECT  Matricule, Etudiant, CodeCours, Cours, Programme,
                Session, DateDebut, DateFin, DateInscription, Note,
                ProfesseurPrincipal, Salle,
                CASE
                    WHEN Note IS NULL AND DateFin < CAST(GETDATE() AS DATE) THEN N'Note manquante'
                    WHEN Note IS NULL THEN N'En attente'
                    WHEN Note >= 60   THEN N'Réussite'
                    ELSE                   N'Échec'
                END AS Resultat
        FROM dbo.vw_ListeInscriptions
        WHERE (@CodeSession IS NULL OR CodeSession = @CodeSession)
          AND (@CodeCours   IS NULL OR CodeCours   = @CodeCours)
          AND (@Recherche   IS NULL
               OR Etudiant LIKE N'%' + @Recherche + N'%'
               OR CAST(Matricule AS VARCHAR(10)) = @Recherche)
        ORDER BY DateDebut DESC, Cours, Etudiant;";

    // Sessions pour le filtre, avec leur état (terminée, en cours, à venir)
    const string REQUETE_SESSIONS = @"
        SELECT  CodeSession,
                Libelle + CASE
                              WHEN DateFin < CAST(GETDATE() AS DATE)   THEN N' (terminée)'
                              WHEN DateDebut > CAST(GETDATE() AS DATE) THEN N' (à venir)'
                              ELSE                                          N' (en cours)'
                          END AS Texte
        FROM dbo.Session
        ORDER BY DateDebut DESC;";

    // Cours pour le filtre (lus dans la vue du catalogue)
    const string REQUETE_COURS = @"
        SELECT  CodeCours, Description + N' (' + CodeCours + N')' AS Texte
        FROM dbo.vw_ListeCours
        ORDER BY Description;";

    // Colonne et sens du tri choisis en cliquant sur un titre.
    // Le ViewState les garde d'un clic à l'autre (postbacks).
    private string TriColonne
    {
        get { return (string)ViewState["TriColonne"]; }
        set { ViewState["TriColonne"] = value; }
    }

    private string TriSens
    {
        get { return (string)(ViewState["TriSens"] ?? "ASC"); }
        set { ViewState["TriSens"] = value; }
    }

    protected void Page_Load(object sender, EventArgs e)
    {
        if (!IsPostBack)
        {
            try
            {
                RemplirListe(ddlSession, REQUETE_SESSIONS, "CodeSession", "Toutes les sessions");
                RemplirListe(ddlCours, REQUETE_COURS, "CodeCours", "Tous les cours");
            }
            catch (SqlException ex)
            {
                AfficherErreur(ex);
                return;
            }
            AfficherInscriptions();
        }
    }

    // Changement de session ou de cours, ou clic sur « Rechercher »
    protected void Filtre_Change(object sender, EventArgs e)
    {
        gvInscriptions.PageIndex = 0;
        AfficherInscriptions();
    }

    protected void btnEffacer_Click(object sender, EventArgs e)
    {
        ddlSession.SelectedIndex = 0;
        ddlCours.SelectedIndex = 0;
        txtRecherche.Text = "";
        TriColonne = null;
        gvInscriptions.PageIndex = 0;
        AfficherInscriptions();
    }

    // Clic sur un titre de colonne : 1er clic = croissant, 2e clic = décroissant
    protected void gvInscriptions_Sorting(object sender, GridViewSortEventArgs e)
    {
        if (TriColonne == e.SortExpression)
        {
            TriSens = (TriSens == "ASC") ? "DESC" : "ASC";
        }
        else
        {
            TriColonne = e.SortExpression;
            TriSens = "ASC";
        }
        gvInscriptions.PageIndex = 0;
        AfficherInscriptions();
    }

    // Clic sur un numéro de page sous la liste
    protected void gvInscriptions_PageIndexChanging(object sender, GridViewPageEventArgs e)
    {
        gvInscriptions.PageIndex = e.NewPageIndex;
        AfficherInscriptions();
    }

    // Pour chaque ligne affichée : couleur de l'étiquette « Résultat »
    protected void gvInscriptions_RowDataBound(object sender, GridViewRowEventArgs e)
    {
        if (e.Row.RowType != DataControlRowType.DataRow)
        {
            return;
        }

        Label etiquette = (Label)e.Row.FindControl("lblResultat");
        string classe;
        switch (etiquette.Text)
        {
            case "Réussite": classe = "resultat-reussite"; break;
            case "Échec": classe = "resultat-echec"; break;
            case "Note manquante": classe = "resultat-manquante"; break;
            default: classe = "resultat-attente"; break;
        }
        etiquette.CssClass = "etiquette " + classe;
    }

    // Lit la vue avec les filtres choisis, puis remplit la grille et le résumé
    private void AfficherInscriptions()
    {
        DataTable inscriptions = new DataTable();

        try
        {
            using (SqlConnection connexion = new SqlConnection(CONNECTION_STRING))
            using (SqlCommand commande = new SqlCommand(REQUETE_INSCRIPTIONS, connexion))
            {
                commande.Parameters.Add("@CodeSession", SqlDbType.Char, 5).Value = ValeurOuNull(ddlSession.SelectedValue);
                commande.Parameters.Add("@CodeCours", SqlDbType.VarChar, 10).Value = ValeurOuNull(ddlCours.SelectedValue);
                commande.Parameters.Add("@Recherche", SqlDbType.NVarChar, 50).Value = ValeurOuNull(txtRecherche.Text);

                using (SqlDataAdapter adaptateur = new SqlDataAdapter(commande))
                {
                    adaptateur.Fill(inscriptions);   // ouvre la connexion, lit, referme
                }
            }
        }
        catch (SqlException ex)
        {
            AfficherErreur(ex);
            return;
        }

        // Tri choisi en cliquant sur un titre (sinon : l'ordre de la requête)
        DataView vue = inscriptions.DefaultView;
        if (!string.IsNullOrEmpty(TriColonne))
        {
            vue.Sort = TriColonne + " " + TriSens;
        }

        gvInscriptions.DataSource = vue;
        gvInscriptions.DataBind();

        int nombre = inscriptions.Rows.Count;
        lblNombre.Text = nombre + (nombre > 1 ? " inscriptions trouvées." : " inscription trouvée.");
        AfficherResume(inscriptions);
    }

    // Résumé de la barre latérale, calculé sur les lignes trouvées
    private void AfficherResume(DataTable inscriptions)
    {
        HashSet<int> etudiants = new HashSet<int>();
        int notesSaisies = 0, enAttente = 0, manquantes = 0, reussites = 0;
        decimal somme = 0;

        foreach (DataRow ligne in inscriptions.Rows)
        {
            etudiants.Add(Convert.ToInt32(ligne["Matricule"]));

            if (ligne["Note"] == DBNull.Value)
            {
                if ((string)ligne["Resultat"] == "Note manquante") manquantes++;
                else enAttente++;
            }
            else
            {
                decimal note = Convert.ToDecimal(ligne["Note"]);
                notesSaisies++;
                somme += note;
                if (note >= 60) reussites++;
            }
        }

        litInscriptions.Text = inscriptions.Rows.Count.ToString();
        litEtudiants.Text = etudiants.Count.ToString();
        litNotesSaisies.Text = notesSaisies.ToString();
        litEnAttente.Text = enAttente.ToString();
        litManquantes.Text = manquantes.ToString();
        // La culture fr-CA (ligne Page du .aspx) donne la virgule décimale : 78,5
        litMoyenne.Text = notesSaisies > 0 ? (somme / notesSaisies).ToString("0.#") : "—";
        litReussite.Text = notesSaisies > 0 ? (100m * reussites / notesSaisies).ToString("0") + "\u00A0%" : "—";
    }

    // Remplit une liste déroulante : un premier choix « Tous », puis les lignes de la requête
    private static void RemplirListe(DropDownList liste, string requete, string colonneValeur, string texteTous)
    {
        DataTable lignes = new DataTable();
        using (SqlConnection connexion = new SqlConnection(CONNECTION_STRING))
        using (SqlDataAdapter adaptateur = new SqlDataAdapter(requete, connexion))
        {
            adaptateur.Fill(lignes);
        }

        liste.Items.Clear();
        liste.Items.Add(new ListItem(texteTous, ""));
        foreach (DataRow ligne in lignes.Rows)
        {
            liste.Items.Add(new ListItem(ligne["Texte"].ToString(), ligne[colonneValeur].ToString()));
        }
    }

    // Texte vide -> NULL (pas de filtre) ; sinon le texte sans espaces autour
    private static object ValeurOuNull(string texte)
    {
        texte = (texte ?? "").Trim();
        if (texte.Length == 0)
        {
            return DBNull.Value;
        }
        return texte;
    }

    private void AfficherErreur(SqlException ex)
    {
        lblErreur.Text = Server.HtmlEncode(
            "Impossible d'afficher les inscriptions. Détail technique : " + ex.Message);
        lblErreur.Visible = true;
        pnlFiltres.Visible = false;
    }
}
