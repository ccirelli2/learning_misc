# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:06:38 2017

@author: Chris.Cirelli
"""


from simple_salesforce import Salesforce

Username_chris = 'chris.cirelli@starrcompanies.com'
Password_chris = 'Work4starr!'
Token_chris = 'TvzoSyEjnGTMPYQsBfWXKH6Z'

sf = Salesforce(username= Username_chris, password= Password_chris, security_token= Token_chris)

sf.search("FIND (Murphy)")