# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:08:24 2020

@author: chris.cirelli
"""

from pandasql import sqldf, load_meat
pysqldf = lambda q: sqldf(q, globals())

data_meat = load_meat()

test = pysqldf("SELECT beef from data_meat LIMIT 5;")

print(test)