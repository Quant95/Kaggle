# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:44:24 2020

@author: huzhj
"""


import csv


Path = 'link.csv'
with open(Path,'r',encoding='utf-8',errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        com_row = '"'+row['访问路径'] + '": "' + row['栏目名字'] + '"'
        print(com_row)
f.close()