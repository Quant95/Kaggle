#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:33:18 2020

@author: huzhj
"""
import urllib
from urllib import request
import re

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/71.0.3578.98 Safari/537.36"
}

key = "自学"
#http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule 删去_o
url = "http://fanyi.youdao.com/translate?"
#post的请求需要提交的参数
fromdata = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15789837562241",
        "sign": "f50bed4be11c0c2b84fb7fd32fc0bfd0",
        "ts": "1578983756224",
        "bv": "59a2ee1b62619c43589e27bb52c2517a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
        }
data = urllib.parse.urlencode(fromdata).encode(encoding='utf-8')

req = request.Request(url, data=data, headers=header)

resp = request.urlopen(req).read().decode()

pat = r'"tgt":"(.*?)"}]]'
result = re.findall(pat, resp)