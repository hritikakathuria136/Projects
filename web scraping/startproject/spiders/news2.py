
import scrapy

import re
import codecs


class News2Spider(scrapy.Spider):
    name = "news2"
    start_urls = [
        'https://www.nbcnews.com/search/?q=earthquakes',
    ]
    
    def parse(self, response):
        
        articles = response.css('div[class="gsc-webResult gsc-result"]')
        for article in articles:
            yield {
                "article":article,
                "link": article.css("div[class='gs-title'] a::attr(href)").get(),
                "date": article.css("span.date::text").get(),
                "headline": article.css("h2.headline a::text").get(),
                "author": article.css("span.author::text").get(),
            }