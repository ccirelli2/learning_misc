# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:17:46 2017

@author: Chris.Cirelli
"""

import PyPDF2 as pdf
import nltk
import string


File = pdf.PdfFileReader('C:\\Users\\Chris.Cirelli\\Desktop\\2017 Chubb D&O Application-.pdf')


File.decrypt()

#   Call # of Pages
#num_pages = File.getDocumentInfo()
#
print(num_pages)
#
##   Call Single Page
##Page_0 = File.getPage(0)
##print(Get_page)
#
##   Extract Text
#
##Page_1 = File.getPage(1)
##extract = Page_1.extractText()
##print(extract)
#
#File = pdf.PdfFileReader('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\Pension Plan vs Maximus Inc.pdf')
#
##   Extract text of entire document and pass to list
#List = []
#num_pages = File.getNumPages()
#for x in range(0,num_pages):
#    content = File.getPage(x).extractText().split("\n")
#    List.append(nltk.word_tokenize(str(content)))
#
#
#from nltk.tokenize import RegexpTokenizer
#
#tokenizer = RegexpTokenizer(r'\w+')
#List_nopunc = tokenizer.tokenize(str(List))
#
#from nltk.collections import*
