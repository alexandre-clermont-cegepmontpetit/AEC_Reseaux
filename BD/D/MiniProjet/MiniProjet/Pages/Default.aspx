<%@ Page Title="" Language="C#" MasterPageFile="~/MasterPage.master" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
        <meta name="keywords" content="formation, maisonneuve" />
    <script type="text/javascript" src="http://code.jquery.com/jquery-latest.js">
</script>
    <script type="text/javascript">
$(function(){ 
  $('li:has(ul)') // tete de sous-liste  
    .css('font-weight', 'bold')  
    .css('cursor', 'pointer') 
    .click( function (event){ 
      if (this == event.target) { 
        $(this).children().toggle(1000);   // Affiche ou cache les éléments correspondants
      } 
      // annulation de la propagation  
      return false; 
    } ) 
    .click(); // masquage initial  
  $('li:not( :has(ul) )') // element sans sous-liste  
    .css('color', 'white') 
    .css('cursor', 'default'); 
} ); 
</script>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">

</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="Contenu" Runat="Server">
    <h3>Accueil</h3>
    <hr/>     
    <p>
        Nous offrons les formations suivantes</p>
    
    <div >  
        <ul runat="server">
            <li runat="server">ASP.NET débutant
            <ul  runat="server">
                <li id="subMenuItem1" runat="server">Web Forms</li>
                <li id="Li1" runat="server">Web controles</li>
            </ul>
            </li>
            <li runat="server">ASP.NET intermédiaire
             <ul  runat="server">
                <li id="subMenuItem2" runat="server">Web Forms</li>
                <li id="Li3" runat="server">Web controles</li>
            </ul>
                </li>
            <li runat="server">ASP.NET avancé
             <ul  runat="server">
                <li id="subMenuItem3" runat="server">Web Forms</li>
                <li id="Li4" runat="server">Web controles</li>
            </ul>
            </li>
        </ul>
    </div>
</asp:Content>

