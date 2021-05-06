#!/usr/bin/env python
# encoding: utf-8
'''
@project : weather
@file    : toutiao.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-04-20 22:19
'''


import scrapy
import os


class IndexSiteMapSpider(scrapy.Spider):
    # identifies the Spider.
    name = "toutiao"

    # scrapy crawl index
    def start_requests(self):
        urls = [
            'https://www.tianqi.com/toutiao',
        ]
        items = ['', 'hots', 'haowu', 'shenghuo']
        for it in items:
            if it == '':
                url = urls[0] + '/'
            else:
                url = urls[0] + '/' + it + '/'
            print(url)

            yield scrapy.Request(url=url, callback=self.index)

    def index(self, response):
        # # https://lishi.tianqi.com
        # # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "toutiao", 'toutiao.html')
        # filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\toutiao", "toutiao", 'toutiao.html')
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        last_page_url = response.css('div.pagebox a[title="尾页"]').css('a::attr(href)').extract()[0]  # '/toutiao/100/index.html'
        pages_cnt = int(last_page_url.split("/")[-2])
        for p in range(2, pages_cnt + 1):
            url = 'https://www.tianqi.com' + '/toutiao/' + str(p) + '/index.html'
            yield scrapy.Request(url=url, callback=self.get_one_page)

    def get_one_page(self, response):
        # https://www.tianqi.com/toutiao/2/index.html
        page = int(response.url.split("/")[-2])

        # # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "toutiao", f'page_{page}.html')
        # filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\toutiao", "toutiao", f'page_{page}.html')
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        articles = []
        for a in response.css('div.r ul.toutiao600 li a'):
            title = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            articles.append({title: href})
            print(href)

            yield scrapy.Request(url=href, callback=self.article)

    def article(self, response):
        # https://www.tianqi.com/toutiao/read/46614.html
        num = response.url.split("/")[-1].split(".")[0]
        kind = response.url.split("/")[-2]
        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "toutiao", f'{kind}.{num}.html')
        # filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "toutiao", f'{kind}.{num}.html')
        filename = os.path.join(r"E:\PythonWorkspace\weather_spider\save", "toutiao", f'{kind}.{num}.html')
        with open(filename, 'wb') as f:
            f.write(response.body)


