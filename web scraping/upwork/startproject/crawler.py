from scrapy.crawler import CrawlerProcess
from startproject.spiders.web2 import Web2Spider

process = CrawlerProcess()
process.crawl(Web2Spider)
process.start()