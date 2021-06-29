# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:18:53 2017

@author: Chris.Cirelli
"""

#   PART OF SPEECH TAGGING - NLTK WITH PYTHON

#   Step1: Vocabulary
#Part of speech tagging - each word of a text will be tagged with its word type.  Exs: verb, pronoun, adverb, etc. 

#   Step2: import modules

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer #Unsupervised machine learning tokenizer. You can train it if you want. 

#   Step3: Sample text

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize('sample_text')

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words) #pos stands for part of speech tag. 
            print(tagged)
    except Exception as e:
        print(str(e))

import nltk
text_tokenized = nltk.word_tokenize(sample_text)
token_pos = nltk.pos_tag(text_tokenized)


def shit_fuk():
    for x in token_pos:
        import numpy as np
        list = []
        list.append(x)
        np = np.array(list)
        print(np)


# POS Index 
        #https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

#   Try out on SCA

import nltk
from nltk.tokenize import word_tokenize
import PyPDF2 as pdf

#   Step2: Import File & Extract Text

File = 'C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA Docs\\201788_f01c_17CV02127.pdf'
File2 = pdf.PdfFileReader(File)
x = File2.getNumPages()
List = []
for page in range(0, x):
    content = File2.getPage(page).extractText().split("\n")
    content_tokenized = str(content)
    List.append(content_tokenized)

text_list = nltk.word_tokenize(str(List))
text_wpunc = nltk.Text(text_list)

text_pos = nltk.pos_tag(text_wpunc)
#print(text_pos)
# Doesn't seem to help out as much as I would have thought. The index positioning that was being used and the type pos of the words was intuitive.
# Maybe certain if then statements could be used. 

x = text_wpunc.findall('alleges')

    
    




