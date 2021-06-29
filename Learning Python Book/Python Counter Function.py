# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 08:10:57 2017

@author: Chris.Cirelli
"""

import pandas as pd

#   Step1: Import Counter
from collections import Counter

#   Create a list of random numbers

List = [1,2,4,5,53,2,6,4,2,4,5,55,4,32]

#   Run function

counts = Counter(List)
#print(type(counts)) #note that it is is own class 'class collections.Counter'
#print(counts) #note how the output is a dictionary with keys that represent each variable. 


#   Count specific variable

specific = counts[3] #reference the variable you want to check for in []
#print(specific) #print results


#   Call most common elements only

common = counts.most_common(3) #note that we continue to refer back to counts and not List as counts refers to the function that we ran on our list. 
#print(common)

Text = 'According to a press release dated September 09, 2008, a judge has signed off on awarding plaintiffs counsel Coughlin Stoia Geller Rudman & Robbins LLP $668 million plus interest for its work on the Enron Corp. securities and Employee Retirement Income Security Act litigation — believed to be the largest award ever in a securities class action. On Monday, Judge Melinda Harmon of the U.S. District Court for the Southern District of Texas also gave final approval to the proposed distribution plan for the more than $7.2 billion settlement reached in the case, which accused Wall Streets largest firms of aiding in the fraud that caused Enrons collapse. Were pleased that the court recognizes the tremendous amount of work, skill and determination required to overcome significant obstacles in this complicated case and recover over $7 billion for defrauded investors, said Patrick Coughlin, chief trial counsel of Coughlin Stoia'

Words = Text.split()

counts2 = Counter(Words)

frequency = counts2.most_common(10)

Df = pd.DataFrame(frequency)

#print(Df)

#   Call a File and Counter most commmon words. 

File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Applied Optoelectronics Inc NasdaqGM AAOI Key Developments.txt')

counts_file = Counter(File)

#   Top 10
common_file_top = pd.DataFrame(counts_file.most_common(10))
#print(common_file)

#   All
common_file_all = pd.DataFrame(counts_file.most_common())
#print(common_file_all)

#   Break up words

with open('C:\\Users\\Chris.Cirelli\\Desktop\\Applied Optoelectronics Inc NasdaqGM AAOI Key Developments.txt') as f:
    lines = f.read().split()

count_lines = Counter(lines)
lines_common = count_lines.most_common()
Df = pd.DataFrame(lines_common)
print(Df)

#==============================================================================
# 
# writer = pd.ExcelWriter('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\Projects\\Test Word Count Earnings Call.xls', engine = 'xlsxwriter')  
# Df.to_excel(writer, sheet_name = 'Data')
# writer.save()
#==============================================================================

#   Read PDF Files pyPDF
https://automatetheboringstuff.com/chapter13/