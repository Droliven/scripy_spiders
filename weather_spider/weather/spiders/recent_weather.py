#!/usr/bin/env python
# encoding: utf-8
'''
@project : weather
@file    : recent_weather.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-04-20 19:09
'''

import scrapy
import os

class IndexSiteMapSpider(scrapy.Spider):
    # identifies the Spider.
    name = "recent_weather"
    # scrapy crawl index
    def start_requests(self):
        urls = [
            'https://www.tianqi.com/chinacity.html',
        ]
        for url in urls:
            print(url)

            yield scrapy.Request(url=url, callback=self.all_city_infos)

    def all_city_infos(self, response):
        # https://www.tianqi.com/chinacity.html
        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "recent_weather", 'chinacity.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "recent_weather", 'chinacity.html')

        with open(filename, 'wb') as f:
            f.write(response.body)

        city_infos = []
        for a in response.css('div.citybox span a'):
            city_name = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://www.tianqi.com' + href
            else:
                url = 'https://www.tianqi.com/' + href

            city_infos.append({city_name: url})
            print(url)

            yield scrapy.Request(url=url, callback=self.city_current)


    def city_current(self, response):
        # https://www.tianqi.com/haidian/
        url = response.url
        if url[-1] == "/":
            city = url.split("/")[-2]
            url_7 = url + "7/"
            url_10 = url + "10/"
            url_15 = url + "15/"
            url_30 = url + "30/"
            url_40 = url + "40/"
        else:
            city = url.split("/")[-1]
            url_7 = url + "/7/"
            url_10 = url + "/10/"
            url_15 = url + "/15/"
            url_30 = url + "/30/"
            url_40 = url + "/40/"

        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "recent_weather", f'{city}.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "recent_weather", f'{city}.html')

        with open(filename, 'wb') as f:
            f.write(response.body)

        yield scrapy.Request(url=url_7, callback=self.recent_period)
        yield scrapy.Request(url=url_10, callback=self.recent_period)
        yield scrapy.Request(url=url_15, callback=self.recent_period)
        yield scrapy.Request(url=url_30, callback=self.recent_period)
        yield scrapy.Request(url=url_40, callback=self.recent_period)


    def recent_period(self, response):
        # https://www.tianqi.com/haidian/7/
        url = response.url
        if url[-1] == "/":
            city = url.split("/")[-3]
            period = url.split("/")[-2]
        else:
            city = url.split("/")[-2]
            period = url.split("/")[-1]

        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "recent_weather", f'{city}.{period}.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "recent_weather", f'{city}.{period}.html')

        with open(filename, 'wb') as f:
            f.write(response.body)


