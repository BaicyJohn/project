<%-- 
    Document   : Category
    Created on : Jan 30, 2018, 2:19:10 PM
    Author     : Vinitha
--%>

<%@page import="javax.swing.JOptionPane"%>
<%@page import="javax.swing.JPanel"%>
<%@page import="java.sql.ResultSet"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<jsp:useBean id="obj" class="db.ConnectionClass"></jsp:useBean>
    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Category</title>

        </head>
        <body >
        <%
            if (request.getParameter("catid") != null) {
                session.setAttribute("catid", request.getParameter("catid"));
            }
            if (request.getParameter("scatid") != null) {
                session.setAttribute("scatid", request.getParameter("scatid"));
            }
            if (request.getParameter("itemid") != null) {
                session.setAttribute("itemid", request.getParameter("itemid"));
            }
        %>

        <%
            if (request.getParameter("itemid") != null) {
                String itemid = request.getParameter("itemid");
                String ins = "insert into tbl_cart(item_id,User_id,Cart_status)values('" + session.getAttribute("itemid") + "','" + session.getAttribute("userid") + "',0)";
                obj.executeCommand(ins);

            }

        %>
        <table frame="below" align="center" width="100%" >
            <tr>

                <td align="center"><img src="../purchase/img/animated-fireworks-image-0094.gif"><font color="#039BE5"><h1 >Shop Now!!!</h1></font></td>
                <td align="center">
                    <img src="../purchase/img/SpecialOfferRd.gif" width="400" height="190">
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <img src="../purchase/img/1600X140_v1.jpeg" height="100" width="100%">  
                </td>
            </tr>
        </table> 
    <from name="frmCategory" >

        <table border="0" align="left" cellpadding="8" width="12%" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)" >

            <tr>
                <td bgcolor="#FAFAFA"><h3>Categories</h3> </td>

            </tr>
            <%                    String id = "";
                String catname = "";
                String sel = "select *from tbl_category";
                ResultSet rs = obj.selectCommand(sel);
                while (rs.next()) {
                    id = rs.getString("Category_id");
                    catname = rs.getString("Category_name");


            %>

            <tr>

                <td><a href="Category.jsp?catid=<%=id%>"  style="text-decoration:none" ><font color="#039BE5"><%=catname%></font></a></td>
            </tr>
            <%

                }

            %>
            <tr>
                <td  bgcolor="#FAFAFA"><h3> Subcategory</h3></td>

            </tr>

            <%                              String scid = "";
                String subcatname = "";

                String sels = "select * from tbl_subcategory s inner join tbl_category c on s.Category_id=c.Category_id where s.Category_id='" + session.getAttribute("catid") + "'";
                ResultSet rss = obj.selectCommand(sels);
                while (rss.next()) {
                    scid = rss.getString("Subcategory_id");
                    subcatname = rss.getString("Subcategory_name");


            %>

            <tr>

                <td><a href="Category.jsp?scatid=<%=scid%>" style="text-decoration:none" ><font color="#039BE5"><%=subcatname%></font></a></td>
            </tr>
            <%
                }
            %>



        </table>
        <table align="center" border="0"  cellpadding="8" bgcolor="#FAFAFA" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.15), 0 6px 20px 0 rgba(0,0,0,0.19)" >

            <%
                String sel2 = "select * from tbl_item  where SubCategory_id='" + session.getAttribute("scatid") + "'";
                ResultSet rs2 = obj.selectCommand(sel2);

                int cnt = 0;
                while (rs2.next()) {

                    String iid = rs2.getString("item_id");
                    String iname = rs2.getString("item_name");
                    String image = rs2.getString("Item_image");
                    String price = rs2.getString("Item_price");

                    if ((cnt % 4) == 0) {
            %><tr><%
                 }

                %>



                <td width="180" align="center" bgcolor="white" >
                    <img src="../Company/ProductImage/<%=image%>" height="150" width="150" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)">
                    <h5 align="center"><font size="3"> <%=iname%></font></h5>
                    <h5 align="center"><font size="3" color="#FFC10">$ <%=price%></font></h5>
                    <font color="#03A9F4">  <b><a href="Category.jsp?itemid=<%=iid%>" style="text-decoration:none" >Add to cart</a></b></font>




                    <%

                        if ((cnt % 4) == 3) {
                    %></tr><%
                                }

                                cnt++;
                            }


                %>     


        </table>        
                <table>
                    <tr>
                        <td><a href="Cart.jsp">ViewCart</a></td>
                    </tr>
                </table>



    </from> 
</body>
</html>
