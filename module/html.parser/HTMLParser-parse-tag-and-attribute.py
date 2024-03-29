#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for a in attrs:
                print(f"-> {a[0]} > {a[1]}")
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for a in attrs:
                print(f"-> {a[0]} > {a[1]}")
        
n = int(input())

parser = MyHTMLParser()

for i in range(n):
    parser.feed(input())