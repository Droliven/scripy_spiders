#!/usr/bin/env python
# encoding: utf-8
'''
@project : weather
@file    : world_recent.py
@author  : Droliven
@contact : droliven@163.com
@ide     : PyCharm
@time    : 2021-04-20 21:00
'''

import scrapy
import os

class IndexSiteMapSpider(scrapy.Spider):
    # identifies the Spider.
    name = "world_recent"
    # scrapy crawl index
    def start_requests(self):
        urls = [
            'https://www.tianqi.com/worldcity.html',

        ]
        for url in urls:
            print(url)

            yield scrapy.Request(url=url, callback=self.all_state_infos)

    def all_state_infos(self, response):
        # https://www.tianqi.com/worldcity.html
        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "world_recent", 'worldcity.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "world_recent", 'worldcity.html')

        with open(filename, 'wb') as f:
            f.write(response.body)

        state_infos = []
        for a in response.css("body div.inter_weather.main div.inter_continent div.continent_t a"):
            state_name = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://www.tianqi.com' + href
            else:
                url = 'https://www.tianqi.com/' + href

            city_infos.append({state_name: url})
            print(url)

            yield scrapy.Request(url=url, callback=self.country_current)


    def country_current(self, response):
        # https://www.tianqi.com/asia/   continent_list chooseBox clearfix
        state = response.url.split("/")[-2]

        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "world_recent", f'{city}.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "world_recent", f'{state}.html')

        with open(filename, 'wb') as f:
            f.write(response.body)

        state_countyies = []
        for a in response.css("body div.inter_weather.main div.inter_continent div.continent_list.chooseBox.clearfix ul li a"):
            country_name = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://www.tianqi.com' + href
            else:
                url = 'https://www.tianqi.com/' + href

            state_countyies.append({country_name: url})
            print(url)

            yield scrapy.Request(url=url, callback=self.city_current)


    def city_current(self, response):
        # https://www.tianqi.com/coutury_india/
        country = response.url.split("/")[-2]

        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "world_recent", f'{country}.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "world_recent", f'{country}.html')

        with open(filename, 'wb') as f:
            f.write(response.body)

        cities = []
        for a in response.css("div.main div.allct_l div.inter_weather div.inter_city a"):
            city_name = a.css('a::text').get(),
            href = a.css('a::attr(href)').extract()[0]
            if href[0] == "/":
                url = 'https://www.tianqi.com' + href
            else:
                url = 'https://www.tianqi.com/' + href

            cities.append({city_name: url})
            print(url)

            yield scrapy.Request(url=url, callback=self.city_current)

    def weather(self, response):
        # https://www.tianqi.com/worldcity/1420108.html
        city = response.url.split("/")[-1]

        # filename = os.path.join("D:\FileData\pythonWorkspace\weather\weather\toutiao", "world_recent", f'{city}.html')
        filename = os.path.join("E:\PythonWorkspace\weather\weather\weather\save", "world_recent", f'{city}.html')

        with open(filename, 'wb') as f:
            f.write(response.body)


