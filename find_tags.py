import requests
from bs4 import BeautifulSoup
from array import *

r = requests.get("https://travel.24tv.ua/yes-onoviv-spisok-naynebezpechnishih-krayin-dlya-podorozhey_n1794194")
page = BeautifulSoup(r.text,'html.parser')
tags = ['table', 'p', 'q', 'tr', 'br', 'object', 'img', 'h1', 'body', 'b', 'center', 'head', 'hr', 'link']
d = dict()
for elem in tags:
    list_tags = page.find_all(elem)
    L = len(list_tags)
    d[elem] = L
print(d)