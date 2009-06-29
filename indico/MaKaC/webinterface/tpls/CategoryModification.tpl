
<table width="90%%" align="center" bgcolor="#808080" border="0">
    <tr>
        <td colspan="3" align="center" bgcolor="#808080"><b><font color="white" size="-1"><%= _("Basic data")%></font></b></td>
    </tr>
    <tr>
        <td bgcolor="#EAEAEA" valign="top"><%= _("Name")%></td>
        <td bgcolor="white" width="100%%"><font size="+2"><b>%(name)s</b></font></td>
        <td rowspan="2" valign="middle" bgcolor="#EAEAEA"><form action="%(dataModificationURL)s" method="POST">%(dataModifButton)s</form></td>
    </tr>
    <tr>
        <td bgcolor="#EAEAEA" valign="top"><%= _("Description")%></td>
        <td bgcolor="white" width="100%%"><b>%(description)s</b></td>
    </tr>
</table>
<br>
<table width="90%%" align="center" bgcolor="#808080" border="0">
    <tr>
        <td align="center" bgcolor="#808080"><b><font color="white" size="-1"><%= _("Contents")%></font></b></td>
    </tr>
    <tr>
        <td bgcolor="white">
            <form action="%(removeItemsURL)s" method="POST">
                %(items)s
                %(locator)s
        </td>
    </tr>
    <tr>
        <td bgcolor="#EAEAEA" align="center">
            <table>
                <tr>
                    <td><input type="submit" class="btn" name="remove" value="<%= _("remove")%>"></td>
                    <td>
                        <input type="submit" class="btn" name="reallocate" value="<%= _("re-allocate")%>">
                        </form>
                    </td>
                    <td>
                        <form action="%(addSubCategoryURL)s" method="POST">
                            <input type="submit" class="btn" value="<%= _("add sub-category")%>">
                        </form>
                    </td>
                    <td>
                        <form action="%(addConferenceURL)s" method="POST">
                            %(addConferenceButton)s
                        </form>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>

