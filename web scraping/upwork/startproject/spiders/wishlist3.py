import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from scrapy import Selector
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from scrapy_selenium import SeleniumRequest

class Wishlist3Spider(scrapy.Spider):
    name = 'wishlist3'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/hz/wishlist/ls/2FQ6FORZLWS4K',
                #   'https://www.amazon.com/hz/wishlist/slv/items?filter=unpurchased&paginationToken=eyJGcm9tVVVJRCI6IjllMTgwZDdkLTRhMzMtNDYzOC04NzYwLWNhN2YzNmZkZTM3YSIsIlRvVVVJRCI6IjE5ZmJiMmZlLTA2NzEtNGZlMi05Mzc5LTUzYTM2NzA2MTc3NyIsIkVkZ2VSYW5rIjotMTh9&itemsLayout=LIST&sort=default&type=wishlist&lid=2FQ6FORZLWS4K&ajax=true'
                  
                  ]

    def start_requests(self):
        # create the webdriver instance
        
        
        options = Options()
        options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"
        self.driver = webdriver.Firefox(options=options)
        self.driver.get('https://www.amazon.com/hz/wishlist/ls/2FQ6FORZLWS4K')

        time.sleep(2)  # Allow 2 seconds for the web page to open
        scroll_pause_time = 1

        screen_height = self.driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1
        while True:
            # scroll one screen height each time
            self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")  
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break
        # soup = BeautifulSoup(self.driver.page_source, "html.parser")

        response = Selector(text = self.driver.page_source)
        for product in response.select('.a-fixed-left-grid.a-spacing-none'):
            rurl = product.css('h2.a-size-base > a.a-link-normal::attr(href)').get()
            link = "https://www.amazon.com/" + rurl
            yield {
                'name': product.css('h2.a-size-base > a.a-link-normal::text').get().strip(),
                'link': link,
                'price': product.css('span.a-price > span::text').get(),
                'rating': product.css('span.a-icon-alt::text').get(),
            }
        self.driver.quit()






        # response = requests.get(self.driver.current_url)
        # soup = BeautifulSoup(self.driver.page_source, "html.parser")
        # # response = TextResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8')
        # # response = self.driver.get(response.url)
        # response = Selector(text = self.driver.page_source)
        # # extract the products
        # # products = self.driver.find_elements_by_css_selector('.a-fixed-left-grid.a-spacing-none')
        # # for product in products:
        # for product in soup.select('.a-fixed-left-grid.a-spacing-none'):
        #     rurl = product.select_one('h2.a-size-base > a.a-link-normal')['href']
        #     link = "https://www.amazon.com/" + rurl
        #     name = product.select_one('h2.a-size-base > a.a-link-normal').get_text(strip=True)
        #     price = product.select_one('span.a-price > span').get_text(strip=True)
        #     rating = product.select_one('span.a-icon-alt').get_text(strip=True)

        #     # yield the extracted information
        #     yield {
        #         'product':product,
        #         'name': name,
        #         'link': link,
        #         'price': price,
        #         'rating': rating
        # }

        # self.driver.quit()

        #     rurl = product.css('h2.a-size-base > a.a-link-normal::attr(href)').get()
        #     link = "https://www.amazon.com/" + rurl
        #     yield {
        #         'name': product.css('h2.a-size-base > a.a-link-normal::text').get().strip(),
        #         'link': link,
        #         'price': product.css('span.a-price > span::text').get(),
        #         'rating': product.css('span.a-icon-alt::text').get(),
        #     }
        # self.driver.quit()

