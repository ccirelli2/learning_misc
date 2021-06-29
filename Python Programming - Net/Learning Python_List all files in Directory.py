# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:55:52 2017

@author: Chris.Cirelli
"""

#   HOW TO IDENTIFY ALL FILES IN A DIRECTORY AND PASS THEM TO A LIST

#   Step1: Import package
import os
from os import listdir
import pandas as pd

#   Step2: Specify the directory
directory_1 = "C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA Docs"

#   Step3: Call function to list files

dir_list = os.listdir(list_dir)

List = []

for x in dir_list:
    List.append("C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA Docs"+x)

Df = pd.DataFrame(List)
    
# Step4: Call PyPDF2 and NLTK libraries to read and tokenize data

for x in List:
    print(x)
    
    