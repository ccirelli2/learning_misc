# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 09:23:31 2017

@author: Chris.Cirelli
"""

#   SCRAPING THE WEB PART II - INTRODUCTION TO APIs AND JSONs

#   API - Application Programming Interfaces

#   JSON - Standard form for transfering data between API's
#        - JavaScript Object Notation


#   Step1: Load JSON File

#import json
#
## Load JSON: json_data
#with open("a_movie.json") as json_file:
#    json_data = json.load(json_file)
#
## Print each key-value pair in json_data
#for k in json_data.keys():
#    print(k + ': ', json_data[k])

###### Explanation not clear.   Need to do more research. 


#   API'S

#Set of protocols for communication with applications. 
#
#import requests
#
#url = 'https://api.openaq.org/v1/cities' #define the direction from where you would like to obtain the data
#r = requests.get(url)    #request info from server and catch in 'r'
#json_data = r.json()     #pull data into a dictionary
#
#for key, value in json_data.items():  #for loop for when you are working with dictionaries
#    print(key + ':', value)
# 

   
# Import requests package
#import requests

# Assign URL to variable: url
#url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network' #note that after teh ? is the api key required to retreive teh information. & I guess seperates the api and t= title

# Package the request, send the request and catch the response: r
#r = requests.get(url)

# Print the text of the response
#print(r.text)


#   WIKIPEDIA API
import requests
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
r = requests.get(url)
json_data = r.json()
pizza_extract = json_data['query']['pages']['24768']['extract'] #nested json files

print(pizza_extract)











