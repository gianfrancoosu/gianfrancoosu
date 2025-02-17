<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/xml">
     <table>
       <xsl:for-each select="annotation">
                     <tr>
                       <td>
                            <xsl:value-of select="target/fragment/text"/>
                       </td>
                       <td>
                            <xsl:value-of select="target/fragment/@progress"/>
                       </td>
                     </tr>
        </xsl:for-each>
      </table>
  </xsl:template>
</xsl:stylesheet>
