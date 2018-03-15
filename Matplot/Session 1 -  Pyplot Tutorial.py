# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:35:35 2017

@author: Chris.Cirelli
"""

#https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

#   Import package

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

File1 = pd.read_csv(r'C:\Users\Chris.Cirelli\Desktop\Python Programing Docs\DataFiles Misc\Wage & Hour Data.csv')
df1 = pd.DataFrame(File1)
Columns_set1 = ['trade_nm', 'NAIC Name', 'st_cd', 'findings_start_date', 'flsa_violtn_cnt']
df2_cut = df1[Columns_set1].iloc[:100].copy()
df2_cut.columns = ['Name', 'Industry', 'State', 'Date', 'Violcation Count']





#   Data type

''' All data types are read into matplotlib as numpy arrays.  Therefore, you can use numpy in conjunction with matplot to plot values. 
'''



#   Example 1: Plot simple y value
'''
plt1 = plt.plot([1,2,3,4])
plt.ylabel('some numbers') #note that I did not have to call the function in rel to the plot. 
plt.xlabel('some numbers')
plt.show()
'''

#   Example 2: Plot x vs. y value
'''
plt2 = plt.plot([1,2,3,4], [1,2,3,16]) #(x, y)
plt.ylabel('some numbers') 
plt.xlabel('some numbers')
plt.show()
'''

#   Plot Using Pandas

'''
DataFrame.plot is both a callable method and a namespace attribute for specific plotting methods of the form DataFrame.plot.<kind>.

DataFrame.plot(x=None, y=None, kind='line', ax=None, subplots=False, sharex=None, sharey=False, layout=None, figsize=None, 
use_index=True, title=None, grid=None, legend=True, style=None, logx=False, logy=False, loglog=False, xticks=None, yticks=None, 
xlim=None, ylim=None, rot=None, 
fontsize=None, colormap=None, table=False, yerr=None, xerr=None, secondary_y=False, sort_columns=False, **kwds)[source]


DataFrame.plot([x, y, kind, ax, ....])	DataFrame plotting accessor and method
DataFrame.plot.area([x, y])	Area plot
DataFrame.plot.bar([x, y])	Vertical bar plot
DataFrame.plot.barh([x, y])	Horizontal bar plot
DataFrame.plot.box([by])	Boxplot
DataFrame.plot.density(**kwds)	Kernel Density Estimate plot
DataFrame.plot.hexbin(x, y[, C, ...])	Hexbin plot
DataFrame.plot.hist([by, bins])	Histogram
DataFrame.plot.kde(**kwds)	Kernel Density Estimate plot
DataFrame.plot.line([x, y])	Line plot
DataFrame.plot.pie([y])	Pie chart
DataFrame.plot.scatter(x, y[, s, c])	Scatter plot
DataFrame.boxplot([column, by, ax, ...])	Make a box plot from DataFrame column optionally grouped by some columns or
DataFrame.hist(data[, column, by, grid, ...])	Draw histogram of the DataFrame’s series using matplotlib / pylab.
'''

#   Define DataSet

df2_cut['Date'] = pd.to_datetime(df2_cut['Date'], yearfirst = True)
#df3 = df2_cut.groupby([x.year for x in df2_cut['Date']])['Name'].count()

#   Plot Bar & Line graphs

Dict = {'A': [1,2,3,4], 
        'B': [5,4,3,6], 
        'C': [0,4,3,6],
        'D': [10,40,30,20]}
df4_dict = pd.DataFrame(Dict)
'''
Line = df3.plot(kind = 'line')
Bar = df3.plot(kind = 'bar')
Area = df3.plot.area()
Bar_mult = df4_dict.plot.bar()
Bar_subplots = df4_dict.plot.bar(subplots = True)
'''

#   Scatter Plot (requires x,y values)
'''
np2darray = np.random.randint(0, 100, size = (100,5))
df5_random = pd.DataFrame(np2darray)
df5_random.columns = ['A', 'B', 'C', 'D', 'E']
df5_random.plot.scatter('A', 'B', s = df5_random['A'])
'''

# Plot a time series



#df3 = df2_cut.groupby([x.year for x in df2_cut['Date']], [x.month for x in df2_cut['Date']])['Name'].count()

df2_year = [x.year for x in df2_cut['Date']]

df2_month = [x.month for x in df2_cut['Date']]


df3 = df2_cut.groupby([df2_year, df2_month])['Violcation Count'].count()

df4 = pd.DataFrame(df3)




    
    


