#https://www.hackerrank.com/challenges/html-parser-part-2/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split("\n"))>1:
            print(">>> Multi-line Comment")
            print(data)
        elif len(data.split("\n"))==1:
            print(">>> Single-line Comment")
            print(data)
          
    def handle_data(self, data):
        if (data != '\n'):
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()