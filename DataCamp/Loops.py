# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 07:40:33 2017

@author: Chris.Cirelli
"""
#==============================================================================
# import numpy as np
# 
# ##Loop over dictionary keys and values. 
# #requires usage of .items() as shown below
# 
# # Definition of dictionary
# europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
#           'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
#           
# # Iterate over europe
# for key, value in europe.items():
#     #print("the capital of " + key + " is " + value)
# 
# If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. 
# To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:
#     
# for x in np.nditer(my_array)     
#==============================================================================

#==============================================================================
# import numpy as np
# 
# A = [1,2,3,4,5]
# 
# A_np = np.array(A)
# 
# for x in A_np:
#     print("inches", x)
#==============================================================================

#==============================================================================
# #To iterate over a DataFrame, you need to use the following format
# 
# #for col, row in cars.iterrows():
#     
# import numpy as np
# import pandas as pd
# 
# cars = pd.DataFrame({ 
#         'cars_per_cap': [809, 731, 588],
#         'country': ['United States', 'Australia', 'Japan'],
#         'drives right': ['True', 'False', 'False']}, index = ['US', 'AUS', 'JAP'])
# 
# print(cars)
# 
# #for col, row in cars.iterrows():
#     #print(col) #prints the index of each row. 
#     #print(pd.DataFrame(row))
#     #print(col, ":", row['cars_per_cap']) print a specific column
# 
# #the below apply function allows you to apply a function to every value in a column.
# #so we create a new column cars["name"] = then the row values cars["country"].apply function.  we have two examples, 
# #apply len or str.upper. 
# 
# cars["name_length"] = cars["country"].apply(str.upper)
# print(cars)
#     
#==============================================================================
    
 
    
    
    
    