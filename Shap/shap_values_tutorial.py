# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 07:18:20 2021
@author: chris.cirelli

Ref: Tutorial
    https://towardsdatascience.com/explain-your-model-with-the-shap-values-bc36aac4de3d
Ref : Shap Documentation
    https://shap.readthedocs.io/en/latest/
"""

###############################################################################
# Import Libraries
###############################################################################
import logging
import os
import sys
import pandas as pd
import numpy as np
import shap

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor

###############################################################################
# Define Directories
###############################################################################
dir_data=r'C:\Users\chris.cirelli\Desktop\repositories\data_misc'
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)


###############################################################################
# Load Data
###############################################################################
data=pd.read_csv(os.path.join(dir_data, 'winequality-red.csv'))


###############################################################################
# Fit Model
###############################################################################
Y = data['quality']
X =  data[['fixed acidity', 'volatile acidity', 'citric acid',
           'residual sugar','chlorides', 'free sulfur dioxide',
           'total sulfur dioxide', 'density','pH', 'sulphates', 'alcohol']]

# Split the data into train and test data:
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
# Build the model with the random forest regression algorithm:
model = RandomForestRegressor(max_depth=6, random_state=0, n_estimators=10)
model.fit(X_train, Y_train)


###############################################################################
# Variable Importance Plot
###############################################################################
shap_values = shap.TreeExplainer(model).shap_values(X_train)
shap.summary_plot(shap_values, X_train, plot_type="bar")

###############################################################################
# Positive & Negative Values
###############################################################################
"""
Feature importance: Variables are ranked in descending order.
Impact: The horizontal location shows whether the effect of that value is
        associated with a higher or lower prediction.
Original value: Color shows whether that variable is high (in red) or low
       (in blue) for that observation.
Correlation: A high level of the “alcohol” content has a high and positive
       impact on the quality rating. The “high” comes from the red color,
       and the “positive” impact is shown on the X-axis. Similarly, we will
       say the “volatile acidity” is negatively correlated with the target variable.
"""
shap.summary_plot(shap_values, X_train)


###############################################################################
# Marginal Contribution Plot
###############################################################################
"""
It tells whether the relationship between the target and a feature is linear,
monotonic or more complex.
Function automatically includes the feature that your chosen variable
interacts most with.
"""
shap.dependence_plot("alcohol", shap_values, X_train)





















