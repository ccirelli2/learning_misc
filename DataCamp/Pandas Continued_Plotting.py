# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:01:44 2017

@author: Chris.Cirelli
"""

#   Plotting with Pandas

#   Step1:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\GOOG.csv')


#   Step2: import data

Google = pd.read_csv('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\GOOG.csv', index_col = 'Date', parse_dates = True)
#parse_dates:  investigate this more, but I think you are telling pandas that Column 'Dates' is of data type dates
#print(Google.head(5))

#   Step3: Plot types

#df.plot(x = 'xyz', y = 'abc') #plot x and y axis of a line graph. 
#df.plot(x = 'xyz', y = 'abc', kind = scatter) #plot x and y axis of a line graph. 
#plt.title() Add a title. 
#specify data to plot = ['XYZ', 'ABC'] and then plot them df.plot(x = 'Month', y = y_columns)
#Other Kinds = box, hist, 


df['Close'].plot()
plt.xlabel('dates')
plt.ylabel('close price')
plt.show()

#   Histogram Options

#bins = number of intervals or bins
#range = extrema of bins, maximum and minimum
#normed = whether to normalize to one (?)
#cumulative = compute Cumulative Distribution Function (CDF) adds up the areas under each bin. 

#   Scatter Plots

#Pandas scatter plots are generated using the kind='scatter' keyword argument. 
#Scatter plots require that the x and y columns be chosen by specifying the x and y parameters inside .plot(). 
#Scatter plots also take an s keyword argument to provide the radius of each circle to plot in pixels.

#   Example:
# Generate a scatter plot
#df.plot(kind = 'scatter', x='hp', y='mpg', s=sizes)

# Add the title
#plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
#plt.xlabel('Horse-power')

# Add the y-axis label
#plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
#plt.show()

############  Need to go back to pandas and understand how to remove titles from data so to be able to name them yourself. 


















