# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 19:40:41 2018

@author: hmohan
"""
import xlrd
import os
import pandas as pd
from datetime import datetime


xl= pd.ExcelFile('/home/hmohan/Desktop/ass-3/ins1.xlsx')
#xl.sheet_names
fd1 = xl.parse('Sheet1')

xl= pd.ExcelFile('/home/hmohan/Desktop/ass-3/vio1.xlsx')
fd2 = xl.parse('Sheet1')

fd=pd.merge(fd2,fd1,on=['serial_number'])

l=[]
try:
    for i in fd['facility_name']:
        l.append(i)
    
    l=set(l)
    l=list(l)
    l.sort()
    print('\n list of business name that have atleast one violation are:\n\n',l)
except Exception as e:
    print (e)    
    
    