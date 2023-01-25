#https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
import xml.etree.ElementTree as etree
#https://docs.python.org/3/library/xml.etree.elementtree.html

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for e in elem:
        depth(e, level)    
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)