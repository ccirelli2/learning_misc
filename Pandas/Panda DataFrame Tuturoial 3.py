# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:56:22 2017

@author: Chris.Cirelli
"""
#==============================================================================
# # www.quandl.com
# 
# import pandas as pd
# import matplotlib.pyplot as plt
#==============================================================================

#==============================================================================
# df = pd.read_excel('C:\\Users\\Chris.Cirelli\\Desktop\\Python Code\\Quandl\\Historical Housing Prices_Roswell GA.xls')
# 
# df2 = pd.DataFrame(df)
# df3 = df2.set_index('Date')
# df3.index_col = 0 #another way to modify the index to use the first column of data in your dataset. 
# print(df3.head(5))
#==============================================================================

#==============================================================================
# plt.plot(df3) #example of how to print a line chart. 
# 
# rename columns
# df3.rename(columns = {'bla bla': 'la la la'}) first is what you want to amend, after : what you want to rename it to. 
# print(df3.head(2)) # note for whatever reason this did not write to the file. 
# 
# df3.to_excel('newexcel.xls') #look to the top right. You have now created a new file.
# df3 = pd.read_excel('new file.xls') #reading that same file. 
# 
# 
# remaning a column
# 
# print(df3.rename(columns = {'Values':'Housing Value'}, inplace = True)) #change a single column. 
#==============================================================================

#==============================================================================
# ##Example of how to change the file type
# 
# df.to_html('file name here')
#==============================================================================



















