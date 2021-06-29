# -*- coding: utf-8 -*-
"""
Purpose : Practicing using pandas concat function.

Spyder Editor
This is a temporary script file.
"""

# Import Libraries ------------------------------------------------------------
import pandas as pd



# Declare DataFrames ----------------------------------------------------------
df1 = pd.DataFrame({}, index=[x for x in range(0, 3)])
df1['a'] = [1, 2, 3]
df1['b'] = ['a', 'b', 'c']
df1['c'] = [1.0, 2.0, 3.0]

df2 = pd.DataFrame({}, index=[x for x in range(0, 3)])
df2['a'] = [4, 5, 6]
df2['b'] = ['d', 'e', 'f']
df2['c'] = [4.0, 5.0, 6.0]

df3 = pd.DataFrame({}, index=[x for x in range(6, 9)])
df3['a'] = [4, 5, 6]
df3['b'] = ['d', 'e', 'f']
df3['c'] = [4.0, 5.0, 6.0]
df3['d'] = [4, 5, 6]

df4 = pd.DataFrame({}, index=[x for x in range(6, 9)])
df4['a'] = ['d', 'e', 'f']
df4['b'] = [4, 5, 6]
df4['c'] = [4.0, 5.0, 6.0]
df4['d'] = [4, 5, 6]



# Test - Concat - Same Columns | Same Data Types | Axis 0
''' 1. Perfectly concatenates the tables and seems to ignore the indices
    2. This concat was tried with both the same and disimilar indices and neither
       changed the outcome, which is to say that the indices does not matter
    3. If we ignore the index then it is replaced with an auto incremented one
    4. Verify Integrity will throw an error if there are similar indice values.
       This would be import if you are concatenating records and want to avoid
       duplicates.
    '''
frames1 = [df1, df2]
concat1 = pd.concat(frames1, axis=0, ignore_index=False)


# Same with Axis = 1
'''Ignores the fact that we have the same columns and instead of appending the
 rows creates columns to the side of d1 with the same names. '''
frames2 = [df1, df2]
concat2 = pd.concat(frames2, axis=1)


# Test - Concat - Disimilar Columns | Axis 0
'''  1. Notice how it create a new column for d and took advantage of the
        disimilar index values.
     2. If we pass join=inner then the disimilar columns are dropped.  Note
     though that this is a set operation, so columns for df1 would also be
     dropped if the did not match with df3'''
frames3 = [df1, df3]
concat3 = pd.concat(frames3, axis=0, join='inner')


# Test - Concat - Disimilar Data Types
''' This is not exactly ideal as the concatenation proceded despite the fact
    the columns with the same column names had different data types.
'''
frames4 = [df3, df4]
concat4 = pd.concat(frames4)

























































