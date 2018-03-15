dd to t# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:45:56 2017

@author: Chris.Cirelli
"""
import pandas as pd
import numpy as np
File = pd.read_excel('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\Private NFP Guidelines.xlsx', index_col = 0)
File_df = pd.DataFrame(File)

##     DATACAMP: PANDAS   ######################################################

#==============================================================================
#   Describing your DataFrame

# 
#   Type
# print(type(File_df)) #returns dataframe. 
# 
#   Shape
# print(File_df.shape) #(rows, columns)
# 
#   Names of Columns
# print(File_df.keys()) #returns the same value as if you used columns.  
# print(File_df.columns)

#   Head & Tail of dataframe
# print(File_df.head(1)) #will show first row including column headers
# print(File_df.head(2)) # will show first two rows including the col headers
# print(File_df.tail(1)) #same thing but the end of the data frame. 

#   Info
#print(File_df.info()) #returns a lot of diff characteristics of your dataframe.1
#==============================================================================


#==============================================================================

#   Data Structure Of a Dataframe

#   Columns = Series
#Specialized feature of a DataFrame.  When you select one column, you are selecting a series. 
    
#   Example:
#print(File_df['Industry']) # returns the industry series. 

#   Show values of the series. 
#Industry = File_df['Industry']
#print(Industry.values)

#   Summary
#Therefore, a series is a one dementional numpy array with a label and a 
#two demensional numpy array with headers. 

#==============================================================================


#==============================================================================

# #   Building Dataframes Lists
# 
# #   Step1: #Identify your lists 
# 
# cities =['Austin', 'Atlanta', 'Nashville']
# signups = [7,12,3]
# visitors = [139, 237, 326]
# weekdays = ['Sun', 'Sun', 'Mon']
# 
# #   Step2: Define your list labels or column labels
#     
# list_labels = ['cities', 'signups', 'visitors']
# list_cols = [cities, signups, visitors] #note that these are defined terms and refer to lists.  #known of a list of lists. 
# 
# #   Step3: Using Pythons List and Zip Functions
# 
# zipped = list(zip(list_labels, list_cols))
# 
# #   Step4: dict() and DataFrame() functions.
#     
# data = dict(zipped) #use Pythons dict() function to create a dictionary. 
# users = pd.DataFrame(data) #use Pandas DataFrame function to create a dataframe. 
# print(users)
# 
# #note that you could add an index at the end of the DataFrame function. 
# 
# #   Step5:  Adding to your DataFrame (Broadcast tequnique)
# 
# users['fees'] = 0
# 
# print(users)
# 
# #   Step6: Amending columns and indexes
# 
# users.columns = ['states', 'signatures', 'guests', 'fees']
# print(users) 
# 
# users.index = ['A', 'B', 'C']
# print(users)
#==============================================================================
#https://docs.python.org/3/tutorial/datastructures.html
#==============================================================================


#==============================================================================
# #   Importing and Exporing Data
# 
# #   Step1: file path
# import pandas as pd
# #file = pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SN_d_tot_V2.0.csv')
# #file.info()
# 
# #   Step2: Adjusting Data
# #Using the function header = none will tell pandas not to use the first row as the column names. 
# #pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SN_d_tot_V2.0.csv', header = None)
# 
# #   Step3: Naming Columns
# # Alternatively, you can name the columns and pass them to the read_csv file function. 
# #col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
# #File = pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SN_d_tot_V2.0.csv', header = None, names = col_names)
# #print(File.head(1))
# 
# #   Step4: Removing negative of 0 value cells
# #pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SN_d_tot_V2.0.csv', header = None, names = col_names, na_values = ' -1')
# #this will replace any negative 1 values with na.
# 
# #   Step5: Exporting Data
# #after you are finished minipulating or amending your data, you can export it to a new file. 
#out_csv = 'sunspots.csv' or out_xlsx = 'sunspots.xlsx'
# # sunspots.to_csv(out_csv) or sunspots.to_excel(out_xlsx)
#==============================================================================










R_SIC.replace([np.inf, -np.inf], np.nan) #convert infinite values to nan
R_SIC.dropna(how = all) #drop all nan values. 











