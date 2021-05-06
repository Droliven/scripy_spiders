import scrapy
import os

class IndexSiteMapSpider(scrapy.Spider):
    # identifies the Spider.
    name = "index"
    # scrapy crawl index
    def start_requests(self):
        urls = [
            'https://blog.csdn.net/s/sitemap_index/index_site_map.xml',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dir = os.path.join(r"E:\PythonWorkspace\scrapy01\save\index")
        filename = 'index_site_map.xml'
        with open(os.path.join(dir, filename), 'wb') as f:
            f.write(response.body)
