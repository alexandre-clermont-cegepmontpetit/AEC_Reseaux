<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="ListeEtudiants.aspx.cs" Inherits="Pages_Administration" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
    <meta name="keywords" content="formation, maisonneuve, administration" />
    <script type="text/javascript">
        function isDelete() {
            return confirm("Voulez-vous supprimer cet étudiant ?");
        }
    </script>
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="Contenu" Runat="Server">
    <h3>Étudiants</h3>
    <hr/>
    <p>Liste des étudiants</p>

    <!-- Message de confirmation ou d'erreur (rempli par le code-behind) -->
    <asp:Label ID="lblMessage" runat="server" EnableViewState="False"></asp:Label>

    <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False"
        DataSourceID="SqlDataSource1" DataKeyNames="Matricule" CellPadding="4" ForeColor="#333333" GridLines="None"
        EmptyDataText="Aucun étudiant."
        OnRowUpdated="GridView1_RowUpdated" OnRowDeleted="GridView1_RowDeleted">
        <AlternatingRowStyle BackColor="White" />
        <Columns>
            <%-- Boutons Modifier / Supprimer : TemplateField pour pouvoir appeler isDelete() --%>
            <asp:TemplateField ShowHeader="False">
                <ItemTemplate>
                    <asp:LinkButton ID="lnkModifier" runat="server" CommandName="Edit" Text="Modifier" CausesValidation="False" />
                    <asp:LinkButton ID="lnkSupprimer" runat="server" CommandName="Delete" Text="Supprimer" CausesValidation="False"
                        OnClientClick="return isDelete();" />
                </ItemTemplate>
                <EditItemTemplate>
                    <asp:LinkButton ID="lnkEnregistrer" runat="server" CommandName="Update" Text="Enregistrer" ValidationGroup="Edition" />
                    <asp:LinkButton ID="lnkAnnuler" runat="server" CommandName="Cancel" Text="Annuler" CausesValidation="False" />
                </EditItemTemplate>
            </asp:TemplateField>

            <%-- Matricule : généré par IDENTITY, jamais modifiable --%>
            <asp:BoundField DataField="Matricule" HeaderText="Matricule" InsertVisible="False" ReadOnly="True" SortExpression="Matricule" />

            <asp:TemplateField HeaderText="Prénom" SortExpression="Prenom">
                <ItemTemplate><%# Eval("Prenom") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtPrenom" runat="server" Text='<%# Bind("Prenom") %>' MaxLength="50" />
                    <asp:RequiredFieldValidator ID="rfvPrenom" runat="server" ControlToValidate="txtPrenom"
                        ErrorMessage="Requis" Display="Dynamic" ValidationGroup="Edition" />
                </EditItemTemplate>
            </asp:TemplateField>

            <asp:TemplateField HeaderText="Nom" SortExpression="Nom">
                <ItemTemplate><%# Eval("Nom") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtNom" runat="server" Text='<%# Bind("Nom") %>' MaxLength="50" />
                    <asp:RequiredFieldValidator ID="rfvNom" runat="server" ControlToValidate="txtNom"
                        ErrorMessage="Requis" Display="Dynamic" ValidationGroup="Edition" />
                </EditItemTemplate>
            </asp:TemplateField>

            <asp:TemplateField HeaderText="Adresse" SortExpression="Adresse">
                <ItemTemplate><%# Eval("Adresse") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtAdresse" runat="server" Text='<%# Bind("Adresse") %>' MaxLength="200" />
                </EditItemTemplate>
            </asp:TemplateField>

            <asp:TemplateField HeaderText="Téléphone" SortExpression="Telephone">
                <ItemTemplate><%# Eval("Telephone") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtTelephone" runat="server" Text='<%# Bind("Telephone") %>' MaxLength="20" />
                    <asp:RequiredFieldValidator ID="rfvTelephone" runat="server" ControlToValidate="txtTelephone"
                        ErrorMessage="Requis" Display="Dynamic" ValidationGroup="Edition" />
                </EditItemTemplate>
            </asp:TemplateField>

            <%-- Date de naissance : format AAAA-MM-JJ, champ HTML5 de type date en modification --%>
            <asp:TemplateField HeaderText="Date de naissance" SortExpression="DateNaissance">
                <ItemTemplate><%# Eval("DateNaissance", "{0:yyyy-MM-dd}") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtDateNaissance" runat="server" TextMode="Date"
                        Text='<%# Bind("DateNaissance", "{0:yyyy-MM-dd}") %>' />
                </EditItemTemplate>
            </asp:TemplateField>

            <asp:TemplateField HeaderText="Courriel" SortExpression="Courriel">
                <ItemTemplate><%# Eval("Courriel") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:TextBox ID="txtCourriel" runat="server" Text='<%# Bind("Courriel") %>' MaxLength="100" />
                    <asp:RequiredFieldValidator ID="rfvCourriel" runat="server" ControlToValidate="txtCourriel"
                        ErrorMessage="Requis" Display="Dynamic" ValidationGroup="Edition" />
                    <asp:RegularExpressionValidator ID="revCourriel" runat="server" ControlToValidate="txtCourriel"
                        ValidationExpression="\S+@\S+\.\S+" ErrorMessage="Courriel non valide" Display="Dynamic" ValidationGroup="Edition" />
                </EditItemTemplate>
            </asp:TemplateField>

            <%-- Sexe : liste déroulante pour respecter CK_Etudiant_Sexe ('F', 'H' ou NULL) --%>
            <asp:TemplateField HeaderText="Sexe" SortExpression="Sexe">
                <ItemTemplate><%# Eval("Sexe") %></ItemTemplate>
                <EditItemTemplate>
                    <asp:DropDownList ID="ddlSexe" runat="server" SelectedValue='<%# Bind("Sexe") %>'>
                        <asp:ListItem Text="" Value="" />
                        <asp:ListItem Text="Homme" Value="H" />
                        <asp:ListItem Text="Femme" Value="F" />
                    </asp:DropDownList>
                </EditItemTemplate>
            </asp:TemplateField>
        </Columns>
        <FooterStyle BackColor="White" ForeColor="#333333" />
        <HeaderStyle BackColor="#336666" Font-Bold="True" ForeColor="White" />
        <PagerStyle BackColor="#336666" ForeColor="White" HorizontalAlign="Center" />
        <RowStyle BackColor="White" ForeColor="#333333" />
        <SelectedRowStyle BackColor="#339966" Font-Bold="True" ForeColor="White" />
        <SortedAscendingCellStyle BackColor="#F7F7F7" />
        <SortedAscendingHeaderStyle BackColor="#487575" />
        <SortedDescendingCellStyle BackColor="#E5E5E5" />
        <SortedDescendingHeaderStyle BackColor="#275353" />
    </asp:GridView>

    <%-- Les champs vides (Adresse, DateNaissance, Sexe) sont envoyés comme NULL
         (ConvertEmptyStringToNull vaut True par défaut). --%>
    <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>"
        SelectCommand="SELECT Matricule, Nom, Prenom, Adresse, Telephone, DateNaissance, Courriel, Sexe
                       FROM dbo.Etudiant
                       ORDER BY Nom, Prenom"
        UpdateCommand="UPDATE dbo.Etudiant
                       SET Nom = @Nom, Prenom = @Prenom, Adresse = @Adresse, Telephone = @Telephone,
                           DateNaissance = @DateNaissance, Courriel = @Courriel, Sexe = @Sexe
                       WHERE Matricule = @Matricule"
        DeleteCommand="DELETE FROM dbo.Etudiant WHERE Matricule = @Matricule">
        <DeleteParameters>
            <asp:Parameter Name="Matricule" Type="Int32" />
        </DeleteParameters>
        <UpdateParameters>
            <asp:Parameter Name="Nom" Type="String" />
            <asp:Parameter Name="Prenom" Type="String" />
            <asp:Parameter Name="Adresse" Type="String" />
            <asp:Parameter Name="Telephone" Type="String" />
            <asp:Parameter Name="DateNaissance" DbType="Date" />
            <asp:Parameter Name="Courriel" Type="String" />
            <asp:Parameter Name="Sexe" Type="String" />
            <asp:Parameter Name="Matricule" Type="Int32" />
        </UpdateParameters>
    </asp:SqlDataSource>
</asp:Content>
