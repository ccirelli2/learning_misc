# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:30:48 2017

@author: Chris.Cirelli
"""

import PyPDF2

File = PyPDF2.PdfFileReader('C:\\Users\\Chris.Cirelli\\Desktop\\2017720_f01c_17CV04106.pdf')

page = File.getPage(2)

page_content = page.extractText()

print(page_content)

