#https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        if attrs:
            for a in attrs:
                print(f"-> {a[0]} > {a[1]}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        if attrs:
            for a in attrs:
                print(f"-> {a[0]} > {a[1]}")
        
n = int(input())

parser = MyHTMLParser()

for i in range(n):
    parser.feed(input())