# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 07:26:07 2017

@author: Chris.Cirelli
"""

##Build a data set for Home Price analysis.
#study variation in housing price markets. 
#Quandl API Key: 1bWAq7PyduK84rShMKmv

import quandl
import pandas as pd
import matplotlib.pyplot as plt


###Pull in housing data from Quandl and plot and print it======================

# df = quandl.get("ZILL/C10302_MLP", authtoken="1bWAq7PyduK84rShMKmv", end_date="2017-06-01")
# print(df.head())
# print(df.tail())
# plt.plot(df)

#==============================================================================


###Read a table from a web page==============================================================================

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#This is a list of all dataframes on this web page
print(fifty_states)

#This is the dataframe of the fifty states
print(fifty_states[0])

#Chose the specific column of that dataframe that you want to print
print(fifty_states[0][0]) #column 0

#Abbreviate the table and use the FMAC/HPI_ format to pull data (note the author pulled FMAC data as opposed to Zillo)
for abbv in fifty_states[0][0][1:]:
    print("FMAC/HPI_" + fifty_states[0][0][1:]) #now you have all fifty states in this format. 
==============================================================================






#==============================================================================
