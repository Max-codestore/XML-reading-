# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET

# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('xml.xml')

# getting the parent tag of
# the xml document
root = tree.getroot()
xml_list=[[],[]]

for i in range(len(root)):
    for m in range(len(root[i])):
        xml_list[0].append(root[i][m].tag)
        xml_list[1].append(root[i][m].text)


print(xml_list)