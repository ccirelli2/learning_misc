# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 07:29:25 2017

@author: Chris.Cirelli
"""

#   Import package

from bs4 import BeautifulSoup
import requests
import json

###   Specify the url: url
#url = "http://securities.stanford.edu/"
#
##   Packages the request, send the request and catch the response: r
#r = requests.get(url)
#
##   Extract the response: text
#
#html_doc = r.text
#soup = BeautifulSoup(html_doc, 'html.parser')
#pretty_soup = soup.prettify()
#print(pretty_soup)


#   IMPORTING PDF FILE FROM STAFORD CLEARINGHOUSE

#from urllib.request import urlretrieve              # call the library 
#import PyPDF2 as pdf
#url = 'http://securities.stanford.edu/filings-documents/1062/SCS00_01/201789_f01c_17CV04665.pdf' #name the url including file location
#urlretrieve(url, '201789_f01c_17CV04665.pdf') #retreive the file
#File = pdf.PdfFileReader('201789_f01c_17CV04665.pdf') #read the file using PyPDF
#Page1 = File.getPage(0).extractText().split("\n") #extract text from first page
#print(Page1) #print first page



url = 'http://securities.stanford.edu'
r = requests.get(url)
text = r.text
soup = BeautifulSoup(text, 'html.parser')
a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))
    