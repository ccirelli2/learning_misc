# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:46:23 2017

@author: Chris.Cirelli
"""
import os
import pandas as pd

Folder = r'C:\Users\Chris.Cirelli\Desktop\Python Programing Docs\Learn Python\9. Book - Automate the Boring Stuff w Python'


List1 = []
for x in os.listdir(Folder):
    List1.append((Folder + '\\' + x))

df1 = pd.DataFrame(List1)

for x in df1.iloc[0]:
    File = open(x, 'r')
    print(File)