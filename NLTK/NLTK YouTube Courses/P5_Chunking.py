# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:49:52 2017

@author: Chris.Cirelli
"""
# https://www.pythonprogramming.net/

#   Finding Noun Phrases

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer(sample_text)

def process_content():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        
        chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><} """  #use tripple quotes. Proceed """ with r to denote a regular expression
        # <> to mention any form of pos tag.
        # Find any adverb
        # . period is any character. 
        # ? so no longer than 1
        # * looking for 0 or more of these
        
        
# Read the normal express syntax prior to this tutorial. 
        
        #https://www.pythonprogramming.net/regular-expressions-regex-tutorial-python-3/
        