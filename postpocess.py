import lxml.etree as ET
from acdh_tei_pyutils.tei import TeiReader


input_file = './uber-den-traum.xml'
tei_dummy = TeiReader('tei-dummy.xml')
crit_app = TeiReader(input_file)
body = tei_dummy.any_xpath('.//tei:ab')[0]
list_wit_node = tei_dummy.any_xpath('.//tei:listWit')[0]
wit_set = set()

for rdg in crit_app.any_xpath('.//tei:rdg/@wit'):
    for w in rdg.split():
        wit_set.add(w[1:])

for x in list(sorted(wit_set)):
    w_node = ET.Element("{http://www.tei-c.org/ns/1.0}witness", nsmap={None: "http://www.tei-c.org/ns/1.0"})
    w_node.attrib['{http://www.w3.org/XML/1998/namespace}id'] = x
    w_node.text = x
    list_wit_node.append(w_node)
for x in crit_app.any_xpath('./*'):
    body.append(x)

tei_dummy.tree_to_file('hansi.xml')