#!/usr/bin/env python
# encoding: utf-8
'''
@project : weather
@file    : main.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-04-20 15:41
'''

from scrapy.cmdline import execute
import os
import sys

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(['scrapy', 'crawl', 'test'])
    # execute(['scrapy', 'crawl', 'history_weather'])
    # execute(['scrapy', 'crawl', 'recent_weather'])
    # execute(['scrapy', 'crawl', 'world_recent'])
    execute(['scrapy', 'crawl', 'toutiao'])

    pass