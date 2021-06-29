# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:51:39 2017

@author: Chris.Cirelli
"""

import pandas as pd

#   IMPORTING FLAT FILE FROM THE WEB

#   Two packages - urllib and request

#   urlib package
#provides an interface for fecthing data across the web
#urlopen() works like the open function but opens ulrs instead of file names

#   HOW TO AUTOMATE FILE DOWNLOAD IN PYTHON

#   Step1: Import package
from urllib.request import urlretrieve 

#   Step2: assign the url as a string to the url
#url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

#   Step3: Write contents of url to file
#urlretrieve(url, 'winequality-red.csv') #python says not found

#   Step4: Create Dataframe of the information
#df = pd.read_csv('winequality-red.csv', sep=';')
#print(df.head())


#   SECOND EXAMPLE - IMPORT FLAT FILE USING PANDAS

#   Step 1: Assign file to url
#url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
#df = pd.read_csv(url, sep = ';') #read into a data frame by defining df, then first argument url, second is the seperater. 
#print(df.head())


#   IMPORT EXCEL FILE USING PANDAS

#   Step1- Assign url
#url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

#   Step2 - Read file to dataframe
#df = pd.read_excel(url, sep = ';')

#   Step3 - Read in all sheets of Excel file: xl
#xl = pd.read_excel(url, sheetname=None)

#   Step4 - Print the sheetnames to the shell
#print(xl.keys())

#   Step5 - Print the head of the first sheet (using its name, NOT its index)
#print(xl['1700'].head())


#   HTTP REQUESTS TO IMPORT FILES FROM WEB

#   URL
#Stands for Uniform/Universal Resource Locator
#   HTTP
#stands for hyper text transfer protocol

#   HTML
#Stands for hyper text markup language, standard markup language for the web


#   EXAMPLE 1

#   Step1 - Call necessary library functions
from urllib.request import urlopen, Request

#   Step2 - Define url
#url = "https://www.wikipedia.org/"

#   Step3 - Package the get request using the request function
#request = Request(url)

#   Step4 - Send the Request and Catch the Response
#response = urlopen(request) #returns an http response object that has an associated read method

#   Step5 - Apply Read Method 
#html = response.read() #returns html as a string as html
#print(type(html))
#print(type(request))

#   Step6 - Remember to be polite and close response
#response.close()


#   EXAMPLE 2: SUING REQUESTS PACKAGE

#   Import packages
from urllib.request import urlopen, Request

#   Specify the url
#url = "http://www.datacamp.com/teach/documentation"

#   This packages the request
#request = Request(url)

# Sends the request and catches the response: response
#response = urlopen(request)

# Extract the response: html
#html = response.read()

# Print the html
#print(html)

# Be polite and close the response!
#response.close()


#   PERFORMING HTTP REQUESTS IN PYTHON USING REQUESTS

#   Import package
#import requests

#   Specify the url: url
#url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
#r = requests.get(url)

# Extract the response: text
#text = r.text

# Print the html
#print(text)


#   BEAUTIFUL SOUP PACKAGE

#   Tag Soup - refers to syntactically incorrect data in html

#   Import packages
import requests
from bs4 import BeautifulSoup

#   Specify url: url
url = 'https://www.python.org/~guido/'

#   Package the request, send the request and catch the response: r
r = requests.get(url)

#   Extract the response as html: html_doc
#html_doc = r.text

#   Create a BeautifulSoup object from the HTML: soup
#soup = BeautifulSoup(html_doc, 'html.parser')

#   Get the title of Guido's webpage: guido_title
#guido_title = soup.title

#   Print the title of Guido's webpage to the shell
#print(guido_title)

#   Get Guido's text: guido_text
#guido_text = soup.get_text()

#   Print Guido's text to the shell
#print(guido_text)


#   GETTING HYPERLINKS

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'http://securities.stanford.edu/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, 'html.parser')

# Print the title of Guido's webpage
#print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags

a_tags = soup.find_all('a')

# Print the URLs to the shell

for link in a_tags:
    print(link.get('href'))
    
#   Some notes about href attribute
    
#The href attribute specifies the URL of the page the link goes to.
#If the href attribute is not present, the <a> tag is not a hyperlin



