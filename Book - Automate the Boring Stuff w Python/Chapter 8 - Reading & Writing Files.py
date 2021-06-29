
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:22:51 2017

@author: Chris.Cirelli
"""

import os
import pandas as pd

#   Directory Commands

# Get current directory

'''os.getcwd'''

# Change dir

'''os.chdir('C:\\Windows')'''

# Create new folder

'''os.makedirs()

for x in range(0,5):
    os.makedirs(str(x))
'''

# Finding File Sizes and Folder Contents

'''
List1 = []
[List1.append(x) for x in os.listdir('C:\\Users\Chris.Cirelli\Desktop')]
print(pd.DataFrame(List1))
'''

# Get file size all files in a directory


def get_totalsize(directory1):
    totalsize = 0
    for filename in os.listdir(directory1):
        totalsize1 = totalsize + os.path.getsize(os.path.join('C:\\Users\Chris.Cirelli\Desktop', filename))
    print(totalsize1)



def get_all_files():
    List1 = []
    Dir = 'C:\\Users\Chris.Cirelli\Desktop'
    for x in os.listdir('C:\\Users\\Chris.Cirelli\\Desktop'):
        List1.append(Dir + '\\' + x)
    df1 = pd.DataFrame(List1)
    df1.to_clipboard(excel = True, sep = True)

  

# Opening and Writing to fillings

''' 
Step1:  Create File

Filename = open('file.txt', 'w') #name file, open in write format.  'w' = write
Filename.write('Hello world!')
Filename.close()

Step2: Append File

Filename = open('filename', 'a')  # 'a' = append
Filename.write('Bacon is better than vegetables')
Filename.close()

Step3: Print Content

content = Filename.read()
print(content)
'''


#   Daving Variables with teh shelve Module

''' This module allows you to save variables to a shelve for later use'''
import shelve

shelfFile = shelve.open('mydata')  # shelve.open() ***creates a file, pass it a file name
                                   # shelfFile = ***this is the creation of the variable that references your shelve file. 
cats = ['Mitzy', 'Trixie', 'Shila']# create your values
shelfFile['cats'] = cats           # name your variable
shelfFile.close()                  # close file. 
'''You should see three new files created in your directory.'''

shelfFile = shelve.open('mydata')
print(shelfFile)                   # check to see that the file was created properly
































