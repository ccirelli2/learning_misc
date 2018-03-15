# -*- coding: utf-8 -*-
'''
Created on Fri Oct 13 07:59:27 2017

@author: Chris.Cirelli
'''

import os
import shutil
import pandas as pd

def get_cur_dir():
    current_dir = os.getcwd()
    print(current_dir)

os.chdir(r'C:\Users\Chris.Cirelli')

def list_dir():
    import pandas    
    the_list = os.listdir()
    df1 = pd.DataFrame(the_list)
    print(df1)
    
os.chdir(r'C:\Users\Chris.Cirelli\Desktop')


#   Copy files & tree


#shutil.copy(file from, file to)
#shutil.copytree(from, to) 


#   Move File

#shutil.move(r'C:\Users\Chris.Cirelli\Desktop\3D Systems.docx', r'C:\Users\Chris.Cirelli\Desktop\Example Folder')


