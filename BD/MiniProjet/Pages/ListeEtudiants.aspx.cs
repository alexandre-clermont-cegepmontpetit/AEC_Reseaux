using System;
using System.Data.SqlClient;
using System.Drawing;
using System.Web.UI.WebControls;

public partial class Pages_Administration : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
    }

    // Après la modification d'une ligne
    protected void GridView1_RowUpdated(object sender, GridViewUpdatedEventArgs e)
    {
        if (e.Exception != null)
        {
            AfficherErreur(e.Exception, false);
            e.ExceptionHandled = true;   // pas de page d'erreur jaune
            e.KeepInEditMode = true;     // l'utilisateur peut corriger sa saisie
        }
        else
        {
            AfficherMessage("Étudiant modifié.", false);
        }
    }

    // Après la suppression d'une ligne
    protected void GridView1_RowDeleted(object sender, GridViewDeletedEventArgs e)
    {
        if (e.Exception != null)
        {
            AfficherErreur(e.Exception, true);
            e.ExceptionHandled = true;
        }
        else
        {
            AfficherMessage("Étudiant supprimé.", false);
        }
    }

    // Traduit les erreurs des contraintes de la base en messages clairs
    private void AfficherErreur(Exception ex, bool suppression)
    {
        SqlException sqlEx = ex.GetBaseException() as SqlException;

        if (sqlEx == null)
            AfficherMessage("Erreur : " + ex.Message, true);
        else if (sqlEx.Number == 2627 || sqlEx.Number == 2601)      // UQ_Etudiant_Courriel
            AfficherMessage("Ce courriel est déjà utilisé par un autre étudiant.", true);
        else if (sqlEx.Number == 547 && suppression)                // FK_Inscription_Etudiant
            AfficherMessage("Impossible de supprimer cet étudiant : il a encore des inscriptions.", true);
        else if (sqlEx.Number == 547)                               // CHECK (date, sexe, courriel)
            AfficherMessage("Une valeur ne respecte pas les règles de la base (ex. : la date de naissance doit être dans le passé).", true);
        else
            AfficherMessage("Erreur de base de données : " + sqlEx.Message, true);
    }

    private void AfficherMessage(string message, bool estErreur)
    {
        lblMessage.Text = Server.HtmlEncode(message);
        lblMessage.ForeColor = estErreur ? Color.Red : Color.Green;
    }
}
