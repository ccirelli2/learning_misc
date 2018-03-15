# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:14:52 2017

@author: Chris.Cirelli
"""

###Learning how to read and write to Excel files with Pandas
# #https://www.youtube.com/watch?v=NyUa9J-9Fho
#==============================================================================

import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_excel('Date Price File.xls'))

df2 = df.set_index('Date')
#print(df2.head())

### Reading specific rows and column===========================================
# 
# 
# df3 = pd.read_excel('Date Price File.xls')
# #print (df3) 
#==============================================================================


### Writing to a new excel file =======================================
# 
# df3.to_excel('New Excel File.xls')
# 
# print(pd.read_excel('New Excel File.xls'))
#==============================================================================


#  Write a new DataFrame to a New File=========================================
# D = pd.DataFrame({'Key1':['pants', 'shoes', 'sneakers', 'shorts'], 'Key 2': ['Red', 'Blue', 'Green', 'Yellow']}, index = [2000, 2001, 2002, 2003])
# 
# D.to_excel('New Excel File.xls')
# 
# D2 = pd.read_excel('New Excel File.xls')
# print(D2)
#==============================================================================
