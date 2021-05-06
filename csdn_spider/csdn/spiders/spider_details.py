import os

import scrapy
import json
from scrapy.selector import Selector

class DetailsSpider(scrapy.Spider):
    # identifies the Spider.
    name = "details"
    # scrapy crawl details -O details.json
    def start_requests(self):
        # dir = os.path.join(r"E:\PythonWorkspace\scrapy01\save\index")
        # filename = 'index_site_map.txt'

        urls = [
            # 只能读取html后缀的文件
            'file:///E:/PythonWorkspace/scrapy01/save/index/index_site_map.xml'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.detail_list)

    def detail_list(self, response):
        details_list = []
        # ab = response.body.css('sitemap loc')

        for article in Selector(text=response.body).xpath('//loc/text()').extract():
            details_list.append(article)
        dir = r"E:\PythonWorkspace\scrapy01\save\details"
        with open(os.path.join(dir, "details.json"), "w") as f:
            json.dump(details_list, f)
        print("保存 details.json文件...")


