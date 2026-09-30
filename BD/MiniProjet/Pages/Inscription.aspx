<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="Inscription.aspx.cs" Inherits="Pages_Inscription" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="Contenu" Runat="Server">
       <h3>Inscription</h3>
    <hr/>
        <p>Pour vous inscrire, veuillez remplir le formulaire suivant. Merci.</p>

     <table style="width:100%;">
            <tr>
                <td class="auto-style1">
                    <asp:Label ID="Label1" runat="server" Text="Prénom:"></asp:Label>
                </td>
                <td class="auto-style2">
                    <asp:TextBox ID="txtPrenom" runat="server"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ErrorMessage="Champ Requis" ControlToValidate="txtPrenom"></asp:RequiredFieldValidator>
                </td>
               
            </tr>
             <tr>
                <td class="auto-style1">
                    <asp:Label ID="Label4" runat="server" Text="Nom:"></asp:Label>
                </td>
                <td class="auto-style2">
                    <asp:TextBox ID="txtNom" runat="server"></asp:TextBox>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ErrorMessage="Champ Requis" ControlToValidate="txtNom"></asp:RequiredFieldValidator>
                </td>
                
            </tr>
            <tr>
                <td class="auto-style1">
                    <asp:Label ID="Label2" runat="server" Text="Courriel:"></asp:Label>
                </td>
                <td class="auto-style2">
                    <asp:TextBox ID="txtCourriel" runat="server"></asp:TextBox>
                    <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" ErrorMessage="Adresse courriel non valide" ValidationExpression="\S+@\S+\.\S+" ControlToValidate="txtCourriel"></asp:RegularExpressionValidator>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ErrorMessage="Champ Requis" ControlToValidate="txtCourriel"></asp:RequiredFieldValidator>
                </td>
                
            </tr>
             <tr>
                <td class="auto-style1">
                    <asp:Label ID="Label5" runat="server" Text="Téléphone:"></asp:Label>
                </td>
                <td class="auto-style2">
                    <asp:TextBox ID="txtPhone" runat="server"></asp:TextBox>
                </td>
                
            </tr>
             <tr>
                <td class="auto-style1">
                    <asp:Label ID="Label6" runat="server" Text="Sexe:"></asp:Label>
                </td>
                <td >
                    <asp:RadioButtonList ID="RadioButtonList1" runat="server" 
                        AutoPostBack="True" OnSelectedIndexChanged="RadioButtonList1_SelectedIndexChanged"
                        RepeatDirection="Horizontal">
                        <asp:ListItem >Femme</asp:ListItem>
                        <asp:ListItem >Homme</asp:ListItem>

                    </asp:RadioButtonList>
                </td>
                
            </tr>
            <tr>
                <td class="auto-style1">
                    Cours choisis</td>
                <td class="auto-style2">
                    <!-- <asp:TextBox ID="txtOp" runat="server" Width="20px"></asp:TextBox>  -->
                    <asp:DropDownList ID="DropDownList1" runat="server">
                        <asp:ListItem Text="ASP.NET débutant" Value="debutant" />
                        <asp:ListItem Text="ASP.NET intermédiaire" Value="intermediaire" />
                        <asp:ListItem Text="ASP.NET avancé" Value="avance" />
                    </asp:DropDownList>
                </td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td class="auto-style1">
                    Date début</td>
                <td>
                    <asp:TextBox ID="txtDate" runat="server" OnTextChanged="afficher_calendrier"></asp:TextBox>
                    <asp:ImageButton ID="ImageButton1" runat="server" ImageUrl="../Images/calendar.jpg" OnClick="ImageButton1_Click" Height="21px" Width="27px" />
                    </td>
                <td class="auto-style2">
                    <asp:Calendar ID="Calendar1" runat="server" BackColor="White" BorderColor="#3366CC" BorderWidth="1px" CellPadding="1" DayNameFormat="Shortest" Font-Names="Verdana" Font-Size="8pt" ForeColor="#003399" Height="200px" Width="220px" Visible="False" OnSelectionChanged="Calendar1_SelectionChanged">
                        <DayHeaderStyle BackColor="#99CCCC" ForeColor="#336666" Height="1px" />
                        <NextPrevStyle Font-Size="8pt" ForeColor="#CCCCFF" />
                        <OtherMonthDayStyle ForeColor="#999999" />
                        <SelectedDayStyle BackColor="#009999" Font-Bold="True" ForeColor="#CCFF99" />
                        <SelectorStyle BackColor="#99CCCC" ForeColor="#336666" />
                        <TitleStyle BackColor="#003399" BorderColor="#3366CC" BorderWidth="1px" Font-Bold="True" Font-Size="10pt" ForeColor="#CCCCFF" Height="25px" />
                        <TodayDayStyle BackColor="#99CCCC" ForeColor="White" />
                        <WeekendDayStyle BackColor="#CCCCFF" />
                    </asp:Calendar>
                </td>
                
            </tr>
            <tr>
                <td class="auto-style1">
                    &nbsp;</td>
                <td>
                    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="S'inscrire" />
                    </td>
                <td class="auto-style2">
                    &nbsp;</td>
                
            </tr>
        </table>

</asp:Content>

