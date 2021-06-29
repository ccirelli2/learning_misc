# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:14:22 2017

@author: Chris.Cirelli
"""
import requests
import webbrowser


#   Open a Web Browser
'''
webbrowser.open('http://inventwithpython.com/')

#This will open up a web page directly from your browser
#I guess you could embed this function in your code to get information off a web page or even for the users benefit.  Think
in a GUI application where you want a button to open the web page.  
#Also, if you could control the web page and search function you could automate getting information from a search.  

'''

#   Download a Web page with reqeusts.get()
'''
url = ('https://automatetheboringstuff.com/files/rj.txt')
get_url = requests.get(url)

print(type(get_url))                            # output 'requets.models.Response.  A response object. 
print(get_url.status_code == requests.codes.ok) # if the status code is equal to the requests code, then the request was successful. 
print(get_url.status_code == 200)               # Note that the HTML code for ok is 200.  Not FOund is 404. 
print(get_url.raise_for_status())               # Also will check to see if there were errors.  In this case the output was None. Use for all get requests

get_text = get_url.text

print(type(get_text))                           # output is a string
print('Document Length = ', '', len(get_text))
print(get_text[:200])
'''

#   Checking for Errors
'''
get_url = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    get_url.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))
'''

#   Write to file
'''
textDocument = open('RomeoAndJuliet.txt', 'wb') #('Title.type', 'write binary')
for chunk in get_url.iter_content(1000000):
    textDocument.write(chunk)
textDocument.close()
'''

#   Write to file
'''
url = ('https://seekingalpha.com/article/4113473-wells-fargos-wfc-ceo-tim-sloan-q3-2017-results-earnings-call-transcript')
get_url = requests.get(url)
get_text = get_url.text                         # This works with pure text files as well. 

File = open('TestFile.txt', 'wb')
for x in get_url.iter_content(1000):            # Note that this generates chunks of bites, hence the wb call. 
    File.write(x)
File.close()
'''

#   HTML Basics

'''Tags:
    <a> tag encloes texts that associated with a link. 
    <p> represents a paragraph. 
    href is the URL that the text links to
    Example:  <a href = 'http://inventwithpython.com'>Python books> Python books

Once downloaded:
    Your html code will be in a single string value. 
'''    

#   Creating a Beautiful Soup Object

import bs4

'''
bs4.BeautifulSoup object must be passed a string containing the HTML to parse. 
bs4.BeautifulSoup will return bs4 object. 
'''

# Example
'''
get_url = requests.get('http://nostarch.com')
get_url.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(get_url.text, 'lxml')  # Alternatively, you could load an HTML text file from your hard drive. 
print(type(noStarchSoup))                               # Output 'bs4.BeautifulSoup'
'''
# Finding an element with select() Method

'''Selectors:
    are like regex expressions.  They look for a pattern in the text. 
    Creates a list of tagged object.  Each tag will be represented separately. 
'''

# Example:
'''
Links = noStarchSoup.select('a')                        # Select allows you to 'select' which html attributes you want to capture. 
print(Links[0])                                         # Print string
print(Links[0].attrs)                                   # attrs shows attributes of html element. 
print(Links[0].getText())
'''

# Example Seeking Alpha Transcripts

res = requests.get('https://seekingalpha.com/earnings/earnings-call-transcripts')
#print(res.status_code == requests.codes.ok)
soup = bs4.BeautifulSoup(res.text, 'html.parser')       #Now you have a bs4 object and can use the library functions/methods. 

# Get all links on webpage

List_href = []
for link in soup.find_all('a'):
    List_href.append(link.get('href'))

import pandas as pd
df1 = pd.DataFrame(List_href)

List1 = []
for x in df1[0]:
    if 'https' not in x:
        List1.append(x)

df2 = pd.DataFrame(List1)

List2 = []
for x in df2[0]:
    if 'article' or 'symbol' in x:
        List2.append(x)

df3 = pd.DataFrame(List2)
print(df3)


#   Example with Wikipedia
'''
url = 'https://www.wikipedia.org/'
res_wiki = requests.get(url)
soup_wiki = bs4.BeautifulSoup(res_wiki.text, 'lxml')
'''


















