# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 06:34:56 2017

@author: Chris.Cirelli
"""

import pandas as pd
import numpy as np
import matplotlib as plt

#   USING PYTHON'S QUANDL LIBRARY

#   Import Qunadl library

import quandl
#int_rates = quandl.get("FMAC/30US", authtoken="1bWAq7PyduK84rShMKmv")

#   Amend start and end dates

int_rates = quandl.get("FMAC/30US", authtoken="1bWAq7PyduK84rShMKmv", start_date = '2000-12-31', end_date= '2016-12-31')


#   Plot Data
int_rates.plot(title = '30 Yr Fixed Mortgage Rates (2000 - 2016')


