# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 07:42:44 2017

@author: Chris.Cirelli
"""

#   Import pandas
import pandas as pd

#   Create a date-time object
date1 = pd.datetime(2017, 10, 1)

#   Pass that pobject to Timestamp
D = pd.Timestamp(date1)
'''print(type(D))'''

#   Call different parts of timestamp
'''
print(D.year)
print(D.day)
print(D.month)
'''

#   Wrote a function to add Year, Month and Day's to the dataframe

date_range = pd.date_range(start = '2017, 10, 1', periods = 5)
df1 = pd.DataFrame(date_range)
df1['Values'] = [1,2,3,4,5]
df1.columns = ['Date', 'Values']

def seperate_dates(dataframe, date_column):
    date_column.apply(pd.Timestamp)
    List_year = []
    List_month = []
    List_day = []
    for x in date_column:
        x = x.year
        List_year.append(x)
    for y in date_column:
        y = y.month
        List_month.append(y)
    for z in date_column:
        z = z.day
        List_day.append(z)
    dataframe['Year'] = List_year
    dataframe['Month'] = List_month
    dataframe['Day'] = List_day

'''
seperate_dates(df1, df1['Date'])
print(df1)
df1_grouped = df1.groupby(['Year', 'Month'])['Values'].count()
'''

#   Try on a large dataframe


File1 = pd.read_excel(r'C:\Users\Chris.Cirelli\Desktop\Booking Report\Financial Lines MTD 10.2.17.xlsx', sheetname = 'Data')
df2_file = pd.DataFrame(File1)
print(df2_file['bound_date'].head())

'''
df3 = df2_file[['Status', 'bound_date', 'written_premium']]
df3['bound_date'].apply(pd.Timestamp)
print(df3['bound_date'].head())
'''
'''
df4 = df3.groupby([x.monthp for x in df3['bound_date']])['written_premium'].sum()
'''









