# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:43:25 2017

@author: Chris.Cirelli
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 06:36:16 2017

@author: Chris.Cirelli
"""
#   Instructions
#https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#yahoo-finance

#   Intro Stock Market Data Analysis with Pandas
#https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/

import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2015, 7, 10) #it would be amazing if you could color code outliers by year. 
end = datetime.datetime(2017, 7, 10) #year, monty, day
Stocks = ['AYI', 'GTLS']

AYI = web.DataReader(Stocks, 'google', start, end)

Day1 = (AYI['Close'])#reference Close variable and Stock Ticker
Day0 = Day1.shift(-1)

Test = (Day0 - Day1)/Day1

#Test['AYI'].plot()#plot a single stock. 

Test['GTLS'].plot()

#==============================================================================
# Day1 = AYI['Close']
# 
# 
# 
# Day0 = Day1.shift(-1) #   Shift an entire column up one in a dataframe. 
# 
# 
# List1 = list(zip(Day1, Day0))
# Df = pd.DataFrame(List1) #still need to add the index. 
# #Test = (Df[1] - Df[0])/Df[0]  #Double check.  May be reversed. 
# 
# print(Df.head(3)) 
#==============================================================================

#==============================================================================
# for x in Test:
#     if x <= -.05: #if x is equal to or less than -5.0%
#         print(x)
#         
#==============================================================================
