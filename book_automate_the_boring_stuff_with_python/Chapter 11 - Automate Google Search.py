# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:57:42 2017

@author: Chris.Cirelli
"""

#   Step 1

import requests, sys, webbrowser, bs4

print('Googling...')

res = requests.get('https://www.google.com/search?q=' + ''.join(sys.argv[1:])) 
''' So essentially we would join to this search any arguments > 0 in index that get passed to the interpreter. '''

#   Step 2

soup = bs4.BeautifulSoup(res.text, 'lxml')
LinkElms = soup.select('.r a')

numOpen = min(5, len(LinkElms))

for i in range(numOpen):
    webbrowser.open('http://google.com' + LinkElms[i].get('href'))
    
    