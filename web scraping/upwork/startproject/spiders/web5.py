import scrapy
import pandas as pd
import re

class Web5Spider(scrapy.Spider):
    name = 'web5'
    
    def __init__(self, *args, **kwargs):
        super(Web5Spider, self).__init__(*args, **kwargs)
        self.df = pd.read_csv('/Users/hritikakathuria/upwork/startproject/PLZ_2021.csv', dtype={'PLZ': str})
        self.df['PLZ'] = self.df['PLZ'].astype(str).str.strip()
        self.pin = self.df['PLZ'].tolist()
        self.pin = set(self.pin)
        print(self.pin)
        self.names_seen = []
       
    
    def start_requests(self):
        for pincode in self.pin:
            url = f'https://www.soziale-teilhabe-kiju.lwl.org/de/fuer-eltern-und-junge-menschen/fruehfoerderung/?cps_search_fruhforderstellen-in-ihrer-nahe-finden={pincode}%09#cps_results_fruhforderstellen-in-ihrer-nahe-finden'
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # Initialize a set to keep track of unique names
        # name_set = set()

        for p in response.xpath('//p[@style="margin:0"]'):
            # Extract field values from the HTML
            name = p.xpath('text()[1]').get().strip()
            
            # Check if the name is unique
            if name in self.names_seen:
                # Add the name to the set
                # name_set.add(name)
                continue
            else:
                self.names_seen.append(name)
                address_street = p.xpath('text()[2]').get().strip()
                address_zipcode, address_city = re.findall(r'(\d{5})\s+(.*)', p.xpath('text()[3]').get().strip())[0]
                email = p.xpath('a[starts-with(@href, "mailto:")]/text()').get()
                telephone = p.xpath('a[starts-with(@href, "tel:")]/text()').get()
                website = p.xpath('a[starts-with(@href, "http")]/@href').get()
                url = response.url
                # Yield the item
                yield {
                    'company_name': name,
                    'address_street': address_street,
                    'address_zipcode': address_zipcode,
                    'address_city': address_city,
                    'contact_email': email,
                    'contact_phone': telephone,
                    'contact_website_url': website,
                    "scrapesource_url":url,
                }