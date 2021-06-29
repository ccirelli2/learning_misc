# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 10:53:18 2017

@author: Chris.Cirelli
"""

#########   DATA CAMP : IMPORTING DATA INTO PYTHON    ###########


#How to import basic text files
#a) Those containing plan text
#b) those containing table data, known as a flat file

#  Step1: assign the file a filename
#  Step2: pass the file name to open and end with 'r' for 'read'
#  Step3:  Asign the text to a variable text by applying file.read()
#  Step4: Close the connection to the file. 
#  Step5: read file by using the print command print(text)

#Write text to an Excel or text file. 
file = open("excelfile.xlm", "w")
file.write("Hello world")
file.write("this is our new text file")
file.close()

#Read text of an existing file
filename = 'text_file.txt'
file = open(filename, mode='r')
Text = file.read()
file.close()
print(text)


# Example 2
file = open('moby_dick.txt',mode= 'r')
# Print it
print(file.read())
# Check whether file is closed
print(file.closed)
# Close file
file.close()
# Check whether file is closed
print(file.closed)


#Print only a few lines of the file
# Read & print the first 3 lines
file = open('C:/Users/Chris.Cirelli/Desktop/Python Code/textfile2.txt', mode='r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#Read text of an existing file
file = open('C:/Users/Chris.Cirelli/Desktop/Python Code/textfile2.txt', mode='r')
text = file.read()
print(text)
file.close()


#######     FLAT FILES            ##############

#Flat files are text files containing unstructured data.  
#  To import this data you would use Numpy or Pandas. 

# You can import as a Numpy array, which means you will need to import numpy
import numpy as np

#Flat files are text files containing unstructured data.  
#  To import this data you would use Numpy or Pandas. 

# You can import as a Numpy array, which means you will need to import numpy
import numpy as np
filename = open('C:\Users\Chris.Cirelli\Desktop\Python Code\testfile2.txt', mode='r')
data = np.loadtxt(filename, delimiter= ',')
print(data)

data = np.loadtxt(filename, delimiter= ',', dtype = str)
print(data) #imports all values as strings. 

#you can use ',' and '\t' for comma-delimited and tab-delimited respectively;



#####         IMPORTING FLAT FILES VIA PANDAS     #################


#form that you will use is the DataFrame. 
#  Step:1 Import pandas as pd

import pandas as pd

xl = pd.ExcelFile("testfile3.xlsx")
xl.sheet_names
[u'Sheet1']
df = xl.parse("Sheet1")
print(df.head())

#### Data Sets using Pandas

import pandas as pd

D = {
     "Years": [2017, 2016, 2015, 2014, 2013],
     "R" : [500, 400, 300, 200, 100],
     "COGS": [300, 250, 200, 150, 100],
     "SGA": [60, 50, 40, 40, 40]
     }

DF = pd.DataFrame(D)

DF.index = D["Years"]#changes names of rows. 
#print(DF)

#Importing Data From a CSV File

#Step 1:  pass file to the variable using the pd.read_csv()










