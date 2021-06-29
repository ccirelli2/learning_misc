# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:16:41 2017

@author: Chris.Cirelli
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day': [1,2,3,4,5,6],
             'Visitors':[43, 53, 34, 45, 64, 34],
             'Bound_rate':[65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats) #create DataFrame


for x in df:
    print(df[x])

        