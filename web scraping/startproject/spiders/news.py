import scrapy
from scrapy.loader import ItemLoader
from startproject.NewsItem import NewsItem
import re
import codecs


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://www.bbc.co.uk/search?q=earthquakes&d=news_gnl'
       
           ]
    
    # def parse(self, response):
    #     for item in response.xpath("//li[@class='ssrcss-ukgi9d-PromoListItem e1f5wbog0']"):
    #         loader = ItemLoader(item=NewsItem(), selector=item)
    #         loader.add_xpath("link", "./div//a/@href")
    #         loader.add_xpath("text", "./div//a//text()")
    #         loader.add_xpath("date", "./ul[@class='ssrcss-w45j7g-MetadataStripContainer e1ojgjhb3']//span[@class='ssrcss-1if1g9v-MetadataText ecn1o5v1']/text()")
    #         yield loader.load_item()
    def parse(self, response):
        
        
        rows = response.xpath('//ul[@class="ssrcss-1020bd1-Stack e1y4nx260"] /li')
        for row in rows:
            # Extract the relevant data from the row
            link = row.css("a::attr(href)").get()
            # yield {
            #     "link": link,
            # }
            yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
        # Extract the information you need from the article page
        title = response.css("h1.article-title::text").get()
        date = response.css("time::attr(datetime)").get()
        author = response.css("div.author span::text").get()
        content = response.css("div.article-content p::text").getall()
        
        # Create a NewsItem object with the extracted information
        news_item = NewsItem()
        news_item["title"] = title
        news_item["date"] = date
        # news_item["author"] = author
        # news_item["content"] = content
        yield news_item
            