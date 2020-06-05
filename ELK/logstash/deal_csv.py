# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:31:44 2020

@author: huzhj
"""

import csv
f = open('out.csv','w',encoding='utf-8')

Path = 'module.csv'
with open(Path,'r',encoding='utf-8',errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    click = [row[1].strip()for row in reader]
    
    
csv_writer = csv.writer(f)
csv_writer.wr