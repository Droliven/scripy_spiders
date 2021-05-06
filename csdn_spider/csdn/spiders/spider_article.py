import scrapy
import json
import os
from scrapy.selector import Selector

class ArticlesSpider(scrapy.Spider):
    # identifies the Spider.
    name = "article"
    # scrapy crawl article -O /Users/hongcai/lhc_data/scrapy/article8.json
    def start_requests(self):
        urls = [
            # 只能读取html后缀的文件
            'file:////E:/PythonWorkspace/scrapy01/save/detail_pages/sitemap_detail_8.xml.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        article_list = []
        for article in Selector(text=response.body).xpath('//loc/text()').extract():
            article_list.append(article)
        dir = r"E:\PythonWorkspace\scrapy01\save\articles"
        with open(os.path.join(dir, "articles.json"), "w") as f:
            json.dump(article_list, f)
        print("保存 articles.json文件...")
