#!/usr/bin/env python
# encoding: utf-8
'''
@project : scrapy01
@file    : main.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-05-06 16:20
'''

from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'index'])
    # execute(['scrapy', 'crawl', 'details'])
    # execute(['scrapy', 'crawl', 'detail_page'])
    # execute(['scrapy', 'crawl', 'article'])
    execute(['scrapy', 'crawl', 'article_page'])


    pass