# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 06:45:34 2017

@author: Chris.Cirelli
"""

#   CH2 ACCESSING TEXT CORPORA

#   GOALS
# What are some of the useful text corporate and lexical resources and how can we access them with Python?
# Which python constructs are most helpful with this work?
# How do we avoid repeating ourselves when writing Python code?

#   ACCESSING TEXT CORPORA

#   Step 1: Load NLTK
import nltk

#   Step2: Load Corpora from NLTK server
#nltk.corpus.gutenberg.fileids() #if printed shows the titles of each book

#   Step3: Loading and naming a particular text
#emma = nltk.corpus.gutenberg.words('austen-emma.txt') #envoking words function. 

#   Step 3: Alternative way to call corpora
#from nltk.corpus import gutenberg
#gutenberg.fileids()
#emma = gutenberg.words('austen-emma.txt')

#   Step4: Run basic statistics on files 
#for fileid in gutenberg.fileids():
#    num_chars = len(gutenberg.raw(fileid)) #number characters in fileid. 
#    num_words = len(gutenberg.words(fileid)) #number of words
#    num_sents = len(gutenberg.sents(fileid)) #number of sentences
#    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid))) #vocabulary complexity or lexical diversity score. 
#    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid) #print averages

#raw() function gives us the contents of the file without any linguistic processing. 
    

#   5: Web and Chat Text 
# NLTK's library also includes text of a less formal nature.  This corpus is called webtext and chattext  
#from nltk.corpus import webtext
#for fileid in webtext.fileids():
    #print(fileid, webtext.raw(fileid)[0:65])

#   6: Printing only the title of each document
#from nltk.corpus import reuters
#reuters.fileids()
#print(reuters.words('training/9865')[:14]) #call word function on corpora, identify a specific file '' and call first 13 words [:14] 
    
    
#   7: Load Your Own Corpus (use for loading earnings calls and lawsuits)
#from nltk.corpus import PlaintextCorpusReader #load nltk program to create a corpus
#corpus_root = '/usr/share/dict' #location on your harddrive where the information is saved
#wordlists = PlaintextCorpusReader(corpus_root, '.*') #plain text initilaizer

#   8: Conditional Frequency Distribution


File = open('C:\\Users\\Chris.Cirelli\\Desktop\\Python Programing Docs\\DataFiles Misc\\SCA.txt').read()
tokens = nltk.word_tokenize(File)
#print(type(tokens))

text_nltk = nltk.Text(tokens)
fq = nltk.FreqDist(text_nltk)


#Fd = FreqDist(tokens)
#from nltk.collections import*

#Bg = bigrams(tokens)
#for x in Bg:
    










