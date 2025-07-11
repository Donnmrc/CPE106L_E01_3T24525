#!/usr/local/opt/python/libexec/bin/python

"""  Scraping Websites with Python3 """

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

print("Python3 Scraping")
print(" ") 

bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1 ) 
print(".....")
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)
