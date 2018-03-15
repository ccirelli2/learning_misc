# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:38:22 2017

@author: Chris.Cirelli
"""

'''Types of Machine Learning

Supervised:
    - is where the scientist supervises and guides the learning process. 
    - with supervised learning the classification of data has already been done. 
    - Regression is also part of supervised learning, where we have known variables and by using past data we try       
    to predict future events.
    - The problem with regression or inductive reasoning is that, the authors words, it is a weaker form of     
    reasoning as it is based on past events. 

Unsupervised:
    - We create an algorithm and throw data at it and let the computer make sense of it. 
    - The machine will classify and group the data. 
    - All Machine Learning is data classification. 


Testing & Training
    - When we train a machine, this is where we give data whcih is pre-classified.  So, for example, giving a 
    machine 0's and 9's to learn to recognize them. 

Challenges:
    - Acquiring Data
    - How you will organize the data. 

scikit has prepopulated datasets that we can use. 

'''


import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn import datasets                    # sklearn has its own datasets. 
from sklearn import svm                         # support vector machine, machine learning algorithm. 

#   Import Datasets

digits = datasets.load_digits()                 # apparently you can look at this dataset somewhere or print it. 

def print_datasets():
    print(digits.data)
    print(digits.target)
    print(digits.images[0])


#   Example:  Predicting values of images
'''    
clf = svm.SVC(gamma = 0.001, C = 100)           # Need to research gamma and C. 

x, y = digits.data[:-1], digits.target[:-1]     # Calling data and targets.  Not x is the dependent and y   
                                                # independent variable. 

clf.fit(x,y)
print('Prediction: ', clf.predict(digits.data[-1]))   #predict what is the first negative element. 
plt.imshow(digits.images[-1], cmap= plt.cm.gray_r, interpolation = 'nearest')
plt.show()
'''


#   Example:  
'''
clf = svm.SVC(gamma = 0.001, C = 100)           # Need to research gamma and C. 

x, y = digits.data[:-10], digits.target[:-10]     # Calling data and targets.  Not x is the dependent and y   
                                                # independent variable. 
                                                # X is the testing.  -10 leaves the last 10 digits in thet set          
                                                # for predicting.         
                                                
clf.fit(x,y)
print('Prediction: ', clf.predict(digits.data[-4]))   #predicting a -2 element 
plt.imshow(digits.images[-4], cmap= plt.cm.gray_r, interpolation = 'nearest')
plt.show()
'''

# Continue with turotial 3: Out Method and Where we will be getting our data. 



















