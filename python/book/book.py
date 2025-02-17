import lxml.etree as ET

dom = ET.parse("./book.xml")
xslt = ET.parse("./book.xsl")
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=False))
