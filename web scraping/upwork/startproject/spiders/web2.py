import scrapy

import re
import codecs


class Web2Spider(scrapy.Spider):
    name = "web2"
    start_urls = [
        'https://bhpagentur.de/zertifizierte-heilpaedagogische-anbieter/',
        
            ]
    
    def parse(self, response):
        
        for tr in response.css('table#tablepress-2 tr'):
            city_zip = tr.css('td.column-2::text').get()
            if city_zip:
                zip_code, city = city_zip.split(' ')[0], city_zip[len(city_zip.split(' ')[0]):].strip()
            else:
                city = None
                zip_code = None   
                    
            phone = tr.css("td.column-4::text").re_first(r'T: (.*)')
            fax = tr.css("td.column-4::text").re_first(r'F: (.*)')
            email = tr.css("td.column-4 a[href^=mailto]::text").get()
            website = tr.css("td.column-4 a[href^=http]::text").get()
            notes = tr.css('td.column-1::text').getall()
            scrapesource_url = 'https://bhpagentur.de/zertifizierte-heilpaedagogische-anbieter/'
            if not tr.css('th'):
                yield {
                    'company_name': tr.css('td.column-1::text').get(),
                    'address_street': tr.css('td.column-3::text').get(),
                    'address_city': city,
                    'address_zipcode':zip_code,
                    'contact_phone': phone,
                    'contact_fax': fax,
                    'contact_email':email,
                    'contact_website_url':website,
                    'company_servicetype_mobility': tr.css('td.column-5::text').get(),
                    'company_notes': ' '.join(notes),
                    'scrapesource_url':scrapesource_url
                }
        
           