#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:06:18 2020

@author: huzhj
"""

import urllib
from urllib import request
import os
import time

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/71.0.3578.98 Safari/537.36"
}

def loadpage(fullurl,filename):
    print("正在下载:", filename)
    req = request.Request(fullurl, headers=header)
    resp = request.urlopen(req).read() #想要下载网页本身， 不需要解码
    return resp

def writepage(html, filename):
    print("正在保存:", filename)
    with open(filename, "wb") as f: #wb二进制方式保存
        f.write(html)
        
    print("-------------------")

#构造url
def tiebaSpider(url, begin, end):
    curpath = os.getcwd()
    for page in range(begin, end+1):
        pn = (page-1)*50
        fullurl = url + "&pn=" + str(pn) #每次请求的完整url
        filename = curpath + "/the" + str(page) + "page.html" #每次请求保存的文件名
        
        html = loadpage(fullurl,filename) #调用爬虫爬取网页
        writepage(html, filename) #把获取到的网页信息写入本地

if __name__ == '__main__':
    kw = input("please input the name of tieba:")
    begin = int(input("please input the beginning page:"))
    end = int(input("please input the ending page:"))
    
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    
    url = url+key
    
    tiebaSpider(url, begin, end)
    time.sleep(10)