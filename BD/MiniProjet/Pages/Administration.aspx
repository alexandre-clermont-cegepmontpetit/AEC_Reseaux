<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="Administration.aspx.cs" Inherits="Pages_Administration" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
     <meta name="keywords" content="formation, maisonneuve, administration" />
    <script type="text/javascript">
        function isDelete() {
            return confirm("Voulez-vous supprimer cette ligne ?");
        }
	</script>
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="Contenu" Runat="Server">
    <h3>Inscriptions</h3>
    <hr/>
    <p>Liste des inscriptions</p>
<p>&nbsp;</p>
<p>
    <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataSourceID="SqlDataSource1" CellPadding="4" DataKeyNames="ID" ForeColor="#333333" GridLines="None">
        <AlternatingRowStyle BackColor="White" />
        <Columns>
            <asp:CommandField ShowDeleteButton="True" ShowEditButton="True" />
            <asp:BoundField DataField="ID" HeaderText="ID" InsertVisible="False" ReadOnly="True" SortExpression="ID" />
            <asp:BoundField DataField="Prenom" HeaderText="Prenom" SortExpression="Prenom" />
            <asp:BoundField DataField="Nom" HeaderText="Nom" SortExpression="Nom" />
            <asp:BoundField DataField="courriel" HeaderText="courriel" SortExpression="courriel" />
            <asp:BoundField DataField="phone" HeaderText="phone" SortExpression="phone" />
            <asp:BoundField DataField="sexe" HeaderText="sexe" SortExpression="sexe" />
            <asp:BoundField DataField="cours" HeaderText="cours" SortExpression="cours" />
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
    <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" 
        DeleteCommand="DELETE FROM [Stagiaire] WHERE [ID] = @ID" 
        InsertCommand="INSERT INTO [Stagiaire] ([Prenom], [Nom], [courriel], [phone], [sexe], [cours]) VALUES (@Prenom, @Nom, @courriel, @phone, @sexe, @cours)" 
        SelectCommand="SELECT [ID], [Prenom], [Nom], [courriel], [phone], [sexe], [cours] FROM [Stagiaire]" 
        UpdateCommand="UPDATE [Stagiaire] SET [Prenom] = @Prenom, [Nom] = @Nom, [courriel] = @courriel, [phone] = @phone, [sexe] = @sexe, [cours] = @cours WHERE [ID] = @ID">
        <DeleteParameters>
            <asp:Parameter Name="ID" Type="Int32" />
        </DeleteParameters>
        <InsertParameters>
            <asp:Parameter Name="Prenom" Type="String" />
            <asp:Parameter Name="Nom" Type="String" />
            <asp:Parameter Name="courriel" Type="String" />
            <asp:Parameter Name="phone" Type="String" />
            <asp:Parameter Name="sexe" Type="String" />
            <asp:Parameter Name="cours" Type="String" />
        </InsertParameters>
        <UpdateParameters>
            <asp:Parameter Name="Prenom" Type="String" />
            <asp:Parameter Name="Nom" Type="String" />
            <asp:Parameter Name="courriel" Type="String" />
            <asp:Parameter Name="phone" Type="String" />
            <asp:Parameter Name="sexe" Type="String" />
            <asp:Parameter Name="cours" Type="String" />
            <asp:Parameter Name="ID" Type="Int32" />
        </UpdateParameters>
    </asp:SqlDataSource>
</p>
    
</asp:Content>



