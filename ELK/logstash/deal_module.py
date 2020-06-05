# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:35:28 2020

@author: huzhj
"""
import csv


Path = 'module.csv'
with open(Path,'r',encoding='utf-8',errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        com_row = '"'+row['访问路径'] + '": "' + row['模块名字'] + '"'
        print(com_row)
f.close()