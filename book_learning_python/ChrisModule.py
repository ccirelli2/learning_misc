# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 19:05:54 2017

@author: Chris.Cirelli
"""

def get_columns(dataframe):
    List1 = []
    for x in dataframe.columns:
        List1.append(x)
    df1_columns = pd.DataFrame(List1)
    print(df1_columns)

def shape(dataframe):
    print(dataframe.shape)

def head(dataframe):
    print(dataframe.head(3))

def dType(dataframe):
    print(type(dataframe))