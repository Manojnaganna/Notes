# What is ASP.NET Web Forms?
ASP.NET Web Forms is a framework within ASP.NET used for building dynamic, data-driven web applications. It follows an event-driven programming model, similar to Windows Forms applications, and allows developers to create web applications with a rich user interface using a drag-and-drop approach. Web Forms use server controls, view state, and postbacks to provide an experience similar to desktop applications.

### Ispost back property

```csharp
public partial class Testing : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        if (!IsPostBack)
        {
            Response.Write("Hello World");
        }
    }

    protected void Button1_Click(object sender, EventArgs e)
    {

    }
}
```

This is the **aspx.cs** page and the below is the **Aspx** page

```aspx
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Testing.aspx.cs" Inherits="Testing.Testing" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Button ID="Button1" runat="server" Text="Button" OnClick="Button1_Click" />  
        </div>
    </form>
</body>
</html>
```

In this when the web page first initillay loaded it will It will show the message 
but when it postback the message disapper because is **IsPostBack** is the page level property

When the postback is true

