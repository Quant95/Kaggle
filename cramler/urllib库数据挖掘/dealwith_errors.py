#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:59:40 2020

@author: huzhj
"""

from urllib import request

list1 = [
        "https://www.baidu.com/",
        "https://www.baidu.com/",
        "https://www.baidu.com/",
        "https://www.jeioamhg.com/",
        "https://www.baidu.com/"
        ]
i=0
for url in list1:
    i = i+1
    try:
        request.urlopen(url)
        print("第", i, "请求完成")
    except Exception as e:
        print(e)