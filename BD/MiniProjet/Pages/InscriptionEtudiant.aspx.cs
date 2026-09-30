using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data; // Utliser le namespace ADO.NET 
using System.Data.SqlClient; // Utliser le namespace dur forunisseur de donnees SQL Server

public partial class Pages_Inscription : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }

    protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        //Response.Write(String.Format("Vous êtes un(e) {0}", RadioButtonList1.SelectedItem.Value) );
    }

    protected void afficher_calendrier(object sender, EventArgs e)
    {

    }
    protected void ImageButton1_Click(object sender, ImageClickEventArgs e)
    {
        Calendar1.Visible = true;
    }
    protected void Calendar1_SelectionChanged(object sender, EventArgs e)
    {
        txtDate.Text = Calendar1.SelectedDate.ToShortDateString();
        Calendar1.Visible = false;
    }


    const string CONNECTION_STRING = @"Data Source=localhost\COURS_BD;Initial Catalog=GestionEcole;Integrated Security=True;Encrypt=False;TrustServerCertificate=True;";



    protected void Button1_Click(object sender, EventArgs e)
    {
        //Response.Write("Validation OK");
        SqlConnection thisConnection = new SqlConnection(CONNECTION_STRING);
        try
        {
            // Ouvrir la  connection
            thisConnection.Open();
            // Créer la commande pour la connection

            SqlCommand thisCommand = thisConnection.CreateCommand();
            // Specifier la requête

            string prenom = txtPrenom.Text;
            string nom = txtNom.Text;
            string courriel = txtCourriel.Text;
            string phone = txtPhone.Text;
            string sexe = RadioButtonList1.SelectedValue;
            string adresse = TextAdresse.Text;
            string date_naissance = txtDate.Text;

            thisCommand.CommandText = "INSERT INTO ETUDIANT VALUES ('" + nom + "','" + prenom + "','"
            + adresse + "','" + phone + "','" + date_naissance + "','" + courriel + "','" + sexe + "')";

            // Executer le DataReader de la commande
            SqlDataReader thisReader = thisCommand.ExecuteReader();

            // Fermer le  reader
            thisReader.Close();
            // Fermer la connection
            thisConnection.Close();

            //Vider les champs
        }
        catch (Exception ex)
        {
            Response.Write("Erreur: " + ex.Message);
        }

    }
}