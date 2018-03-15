# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:58:19 2017

@author: Chris.Cirelli
"""
## Using Pandas DataFrames
import pandas as pd

D = {
     "Years":[2014, 2015, 2016, 2017],
     "Revenues":[100,200,300,400], 
     "COGS":[50, 100, 150, 200],
     "SGA":[10, 20, 30, 40]
     }

df = pd.DataFrame(D)

#df.columns = ["Fuck", "Shit", "Ass", "Poop"] #how to rename your columns


 