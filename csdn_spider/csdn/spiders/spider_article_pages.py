import scrapy
import json

class ArticlePagesSpider(scrapy.Spider):
    # identifies the Spider.
    name = "article_page"
    # scrapy crawl article_page
    def start_requests(self):
        urls = []
        with open('E:/PythonWorkspace/scrapy01/save/articles/articles.json') as f:
            data = json.load(f)
            for detail in data:
                urls.append(detail)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page_name = response.url.split("/")[-1]
        author = response.url.split("/")[-4]
        filename = "E:/PythonWorkspace/scrapy01/save/article_pages/"+author+"-"+page_name+".html"
        with open(filename, 'wb') as f:
            f.write(response.body)
