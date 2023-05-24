from xml.etree.ElementTree import ElementTree

root = ElementTree().parse("complaints.xml")
for i in root.iter():
    print(i)
    print(i.get("id"))
