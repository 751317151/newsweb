'''
@Author: 华豪
@Date: 2019-11-28 18:05:24
@E-Mail: hh@huahaohh.cn
@LastEditors: 华豪
@LastEditTime: 2019-11-28 18:07:21
'''

import requests
from lxml import etree
import pymysql


conn = pymysql.connect("127.0.0.1", 'hh', '92868520', 'newsweb')
cur = conn.cursor()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}