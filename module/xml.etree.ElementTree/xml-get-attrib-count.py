import sys
import xml.etree.ElementTree as etree
#https://docs.python.org/3/library/xml.etree.elementtree.html
#about xml module in python: https://diveintopython3.net/xml.html

def get_attr_number(node):
    count = 0
    for i in node.iter():
        count += len(i.attrib)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))