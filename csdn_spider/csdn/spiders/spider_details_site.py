import scrapy

import json


class DetailsSiteSpider(scrapy.Spider):
    # identifies the Spider.
    name = "detail_page"

    # scrapy crawl detail_page
    def start_requests(self):
        urls = []
        with open(r'E:\PythonWorkspace\scrapy01\save\details\details.json') as f:
            data = json.load(f)
            for detail in data:
                urls.append(detail)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        page_name = response.url.split("/")[-1]
        filename = r"E:/PythonWorkspace/scrapy01/save/detail_pages/" + page_name + ".html"
        with open(filename, 'wb') as f:
            f.write(response.body)
