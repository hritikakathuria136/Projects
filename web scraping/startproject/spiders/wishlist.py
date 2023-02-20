
import scrapy

class WishlistSpider(scrapy.Spider):
    name = "wishlist"
    start_urls = [
        "https://www.amazon.fr/hz/wishlist/ls/2AHRHHHTRX7FE?ref_=wl_share", 
        # "https://www.amazon.fr/hz/wishlist/ls?requiresSignIn=1&ref_=nav_AccountFlyout_wl"
    ]

    def parse(self, response):
        for product in response.css('.a-fixed-left-grid.a-spacing-none'):
            rurl = product.css('h2.a-size-base > a.a-link-normal::attr(href)').get()
            link = "https://www.amazon.fr/" + rurl
            yield {
                'name': product.css('h2.a-size-base > a.a-link-normal::text').get().strip(),
                'link': link,
                'price': product.css('span.a-price > span::text').get(),
                'rating': product.css('span.a-icon-alt::text').get(),
            }
       
