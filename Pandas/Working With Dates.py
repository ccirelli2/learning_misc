# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:04:22 2017

@author: Chris.Cirelli
"""

#   Import package
import datetime

#   Create a datetime object (note order)

today = datetime.date(2017, 10, 1)

#   Time (hours, minutes, seconds)

Time = datetime.time(7, 8, 00)

#   Datetime (combindation)

time_today = datetime.datetime(2017, 10, 1, 7, 8, 00)

#   Time Delta (diff two times)

from datetime import timedelta

date1 = datetime.date(2017, 10, 1)
date2 = datetime.date(2016, 10, 1)

import pandas as pd



