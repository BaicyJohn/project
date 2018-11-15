<%-- 
    Document   : EMI
    Created on : 18 Feb, 2018, 12:41:33 PM
    Author     : AkHiLeSh
--%>

<%@page import="java.sql.ResultSet"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<jsp:useBean id="obj" class="db.ConnectionClass"></jsp:useBean>
<!DOCTYPE html>
<html>
    
                <script src="jquery.js" type="text/javascript"></script>
            <script>
            function bankname(ids)
            {
         
             $.ajax({
                         
                           url: "ajax_bankins.jsp?id=" + ids,
                            
                            
                             success: function(result)
                            {
                                $("#emi").html(result);
                                
                            }   
                          
                        });
                        
                   
            
        }
                   
        </script>
     
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
            <form name="frm">
                
        
        <table cellpadding="8" align="center" style="box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);border-radius: 12px;" >
           
            
            <tr>
                <td rowspan="3">
                    <img src="../purchase/img/bank.png" width="300" height="300">
                </td>
                <td align="center" style="background-color:#81D4FA;" >
                    banks
                </td>
                <td align="center" style="background-color:#81D4FA;">
                    Intrest rate
                </td>
            </tr>
            <tr bgcolor="#FAFAFA" >
                <td rowspan="2">
            <%
                  
           
               if(request.getParameter("submit")!=null) 
                   
               {
                  String bank=request.getParameter("bank");  
                 if(!bank.equals(null))
                   
                   {
                     
                    response.sendRedirect("../purchase/FinalPage.jsp");
                  
               }
                 else 
                 {
                     response.sendRedirect("../purchase/EMI.jsp");
                 }
               }
                
                
                
            String sel="select * from tbl_bank";
            ResultSet rs=obj.selectCommand(sel);
            while(rs.next())
            {
                
            
            
            %>
            <input type="radio" name="bank" value="bank" onclick="bankname(<%=rs.getString("bank_id")%>)"><%=rs.getString("bank_name")%><br><br>
            
             <%
            }
             %>       
                </td>
                <td id="emi" >
   
                </td>
            </tr >
            <tr bgcolor="#FAFAFA">
                <td align="center">
                    <input type="submit" name="submit" size="20" style="background-color:#81D4FA;height:40px; width:150px;border-radius: 12px;box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)" value="PAY &#8377;">
                   
                </td>
            </tr>
        </table>
                </form>
    </body>
</html>
