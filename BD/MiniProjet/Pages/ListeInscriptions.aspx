<%@ Page Title="Liste des inscriptions" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="ListeInscriptions.aspx.cs" Inherits="Pages_ListeInscriptions" Culture="fr-CA" UICulture="fr-CA" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
    <style type="text/css">
        .auto-style1 {
            height: 29px;
        }

        /* ----- Filtres au-dessus de la liste ----- */
        .filtres {
            margin: 10px 0;
            line-height: 2.4;
        }
        .filtres label {
            font-weight: bold;
            margin-right: 4px;
        }
        .filtres select,
        .filtres input[type="text"] {
            margin-right: 14px;
        }

        /* ----- Liste (GridView) : tableau blanc lisible sur le fond sarcelle ----- */
        .grille {
            width: 100%;
            margin: 10px 0 20px;
            border-collapse: collapse;
            background: #ffffff;
            color: #1f2a2a;
        }
        .grille th {
            padding: 7px 8px;
            background: #0e6668;
            color: #ffffff;
            text-align: left;
            white-space: nowrap;
        }
        .grille th a {
            color: #ffffff;            /* titres cliquables pour trier */
        }
        .grille td {
            padding: 6px 8px;
            border-bottom: 1px solid #d3e5e7;
            vertical-align: top;
        }
        .grille tr:nth-child(even) td {
            background: #f1f8f9;
        }
        .grille .nombre {
            text-align: right;
        }
        .grille .sans-coupure {
            white-space: nowrap;
        }
        .grille .detail {
            display: block;
            font-size: 0.9em;
            color: #4c5c5a;
        }
        .grille .pagination td {
            background: #ffffff;
            border: 0;
            padding: 8px 4px;
        }
        .grille .pagination a,
        .grille .pagination span {
            padding: 2px 7px;
        }

        /* ----- Résultat : la couleur aide, le mot reste toujours écrit ----- */
        .etiquette {
            display: inline-block;
            padding: 1px 7px;
            border: 1px solid;
            border-radius: 10px;
            font-weight: bold;
            white-space: nowrap;
        }
        .resultat-reussite { color: #1e6b3f; background: #e4f2e9; }
        .resultat-echec    { color: #9b1c1c; background: #fbeceb; }
        .resultat-attente  { color: #6d5810; background: #faf1d2; }
        .resultat-manquante { color: #ffffff; background: #9b1c1c; }

        /* ----- Résumé dans la barre latérale (sous « Bienvenue! ») ----- */
        .resume-admin {
            padding: 10px 12px;
            color: #ffffff;
        }
        .resume-admin .resume-titre {
            margin: 0 0 8px;
            font-style: italic;
        }
        .resume-admin dl {
            margin: 0;
        }
        .resume-admin dt {
            float: left;
            clear: left;
            width: 62%;
            padding: 3px 0;
        }
        .resume-admin dd {
            margin: 0;
            padding: 3px 0;
            text-align: right;
            font-weight: bold;
        }

        .message-erreur {
            display: block;
            margin: 14px 0;
            padding: 10px 14px;
            background: #ffffff;
            color: #1f2a2a;
            border-left: 6px solid #b3261e;
        }
    </style>
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <%-- Résumé calculé par le code (ListeInscriptions.aspx.cs) --%>
    <div class="resume-admin">
        <p class="resume-titre">Selon les filtres choisis :</p>
        <dl>
            <dt>Inscriptions</dt>
            <dd><asp:Literal ID="litInscriptions" runat="server" Text="0" /></dd>
            <dt>Étudiants</dt>
            <dd><asp:Literal ID="litEtudiants" runat="server" Text="0" /></dd>
            <dt>Notes saisies</dt>
            <dd><asp:Literal ID="litNotesSaisies" runat="server" Text="0" /></dd>
            <dt>En attente</dt>
            <dd><asp:Literal ID="litEnAttente" runat="server" Text="0" /></dd>
            <dt>Notes manquantes</dt>
            <dd><asp:Literal ID="litManquantes" runat="server" Text="0" /></dd>
            <dt>Moyenne</dt>
            <dd><asp:Literal ID="litMoyenne" runat="server" Text="—" /></dd>
            <dt>Taux de réussite</dt>
            <dd><asp:Literal ID="litReussite" runat="server" Text="—" /></dd>
        </dl>
    </div>
</asp:Content>

<asp:Content ID="Content3" ContentPlaceHolderID="Contenu" Runat="Server">

    <h2>Liste des inscriptions</h2>
    <hr />

    <%-- DefaultButton : la touche Entrée dans la zone de recherche lance la recherche --%>
    <asp:Panel ID="pnlFiltres" runat="server" CssClass="filtres" DefaultButton="btnRechercher">
        <asp:Label runat="server" AssociatedControlID="ddlSession" Text="Session :" />
        <asp:DropDownList ID="ddlSession" runat="server" AutoPostBack="True"
            OnSelectedIndexChanged="Filtre_Change" />

        <asp:Label runat="server" AssociatedControlID="ddlCours" Text="Cours :" />
        <asp:DropDownList ID="ddlCours" runat="server" AutoPostBack="True"
            OnSelectedIndexChanged="Filtre_Change" />
        <br />
        <asp:Label runat="server" AssociatedControlID="txtRecherche" Text="Étudiant :" />
        <asp:TextBox ID="txtRecherche" runat="server" MaxLength="50" placeholder="Nom ou matricule" />

        <asp:Button ID="btnRechercher" runat="server" Text="Rechercher" OnClick="Filtre_Change" />
        <asp:Button ID="btnEffacer" runat="server" Text="Effacer les filtres" OnClick="btnEffacer_Click" />
    </asp:Panel>

    <p><asp:Label ID="lblNombre" runat="server" /></p>

    <%-- Les noms (DataField, SortExpression, Eval) sont ceux des colonnes
         de la vue dbo.vw_ListeInscriptions, plus la colonne Resultat
         calculée dans la requête du fichier .aspx.cs.
         Cliquer sur un titre de colonne trie la liste. --%>
    <asp:GridView ID="gvInscriptions" runat="server" AutoGenerateColumns="False"
        GridLines="None" CssClass="grille" PagerStyle-CssClass="pagination"
        AllowSorting="True" OnSorting="gvInscriptions_Sorting"
        AllowPaging="True" PageSize="15" OnPageIndexChanging="gvInscriptions_PageIndexChanging"
        OnRowDataBound="gvInscriptions_RowDataBound"
        EmptyDataText="Aucune inscription ne correspond aux filtres choisis.">
        <Columns>
            <asp:BoundField DataField="Matricule" HeaderText="Matricule" SortExpression="Matricule"
                ItemStyle-CssClass="nombre" HeaderStyle-CssClass="nombre" />

            <asp:BoundField DataField="Etudiant" HeaderText="Étudiant" SortExpression="Etudiant" />

            <%-- Nom du cours, avec son code et son programme en dessous --%>
            <asp:TemplateField HeaderText="Cours" SortExpression="Cours">
                <ItemTemplate>
                    <%# Server.HtmlEncode(Eval("Cours").ToString()) %>
                    <span class="detail"><%# Server.HtmlEncode(Eval("CodeCours") + ", " + Eval("Programme")) %></span>
                </ItemTemplate>
            </asp:TemplateField>

            <asp:BoundField DataField="Session" HeaderText="Session" SortExpression="DateDebut"
                ItemStyle-CssClass="sans-coupure" />

            <asp:BoundField DataField="DateInscription" HeaderText="Inscrit le"
                SortExpression="DateInscription" DataFormatString="{0:yyyy-MM-dd}"
                ItemStyle-CssClass="sans-coupure" />

            <asp:BoundField DataField="Note" HeaderText="Note" SortExpression="Note"
                DataFormatString="{0:0.##}" NullDisplayText="—"
                ItemStyle-CssClass="nombre" HeaderStyle-CssClass="nombre" />

            <%-- Étiquette colorée : la classe CSS est choisie dans gvInscriptions_RowDataBound --%>
            <asp:TemplateField HeaderText="Résultat" SortExpression="Resultat">
                <ItemTemplate>
                    <asp:Label ID="lblResultat" runat="server" Text='<%# Eval("Resultat") %>' />
                </ItemTemplate>
            </asp:TemplateField>

            <asp:BoundField DataField="ProfesseurPrincipal" HeaderText="Professeur"
                SortExpression="ProfesseurPrincipal" />

            <asp:BoundField DataField="Salle" HeaderText="Salle" SortExpression="Salle"
                ItemStyle-CssClass="sans-coupure" />
        </Columns>
    </asp:GridView>

    <%-- Message affiché seulement si la base de données ne répond pas --%>
    <asp:Label ID="lblErreur" runat="server" CssClass="message-erreur" Visible="False" />

</asp:Content>
