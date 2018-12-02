#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/16 10:30
# @Author  : hbw
# @File    : AI133_requests_proxy.py
# @Software: PyCharm
# 1.202.122.239	8060
import requests
from lxml import etree
index=9
ip_url='https://www.kuaidaili.com/free/inha/'+str(index)
html=etree.HTML(requests.get(ip_url).text)
ips=html.xpath('//td[@data-title="IP"]/text()')
ports=html.xpath('//td[@data-title="PORT"]/text()')

# types=html.xpath('//td[@data-title="类型"]/text()')
# 遍历list的时候 获取索引
for i,ip in enumerate(ips): # 在遍历list  返回元素和下标
    port=ports[i]
    print(port)
    proxy={'http':'http://'+ip+':'+port}
    try:
        t=requests.get(url='http://httpbin.org/ip',proxies=proxy,timeout=3).text
        # with open('proxy.txt','a') as w:
        #     w.write(t,port)
        print(requests.get(url='http://httpbin.org/ip',proxies=proxy,timeout=3).text,port)
    except:
        print('异常',proxy)
#{'http':'http://ip:port'}