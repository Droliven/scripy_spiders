#!/usr/bin/env python
# encoding: utf-8
'''
@project : weather
@file    : test.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-04-20 16:56
'''

import scrapy
import os

class IndexSiteMapSpider(scrapy.Spider):
    # identifies the Spider.
    name = "test"
    # scrapy crawl index
    def start_requests(self):
        urls = [
            # 'https://lishi.tianqi.com/acheng/index.html',
            'https://lishi.tianqi.com/suyouqi/202102.html',
        ]
        for url in urls:
            print(url)

            yield scrapy.Request(url=url, callback=self.history_page)

    def all_city_infos(self, response):
        # # https://lishi.tianqi.com
        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", 'lishi.tianqi.index.html')
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        city_infos = []
        for a in response.css('ul.table_list li a'):
            city_name = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://lishi.tianqi.com' + href
            else:
                url = 'https://lishi.tianqi.com/' + href

            city_infos.append({city_name: url})
            print(url)
            yield scrapy.Request(url=url, callback=self.city_all_history)

    def city_all_history(self, response):
        # # https://lishi.tianqi.com/suyouqi/index
        # city = response.url.split("/")[-2]
        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", f'{city}.index.html')
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        city_all_history = []
        for a in response.css('div.lishifengxiang ul.clearfix li a'):
            time = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://lishi.tianqi.com' + href
            else:
                url = 'https://lishi.tianqi.com/' + href

            city_all_history.append({time: url})
            print(url)

            yield scrapy.Request(url=url, callback=self.history_page)

    def history_page(self, response):
        # https://lishi.tianqi.com/suyouqi/202102.html
        city = response.url.split("/")[-2]
        history = response.url.split("/")[-1]
        filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\save", f'{city}.{history}.html')
        with open(filename, 'wb') as f:
            f.write(response.body)


