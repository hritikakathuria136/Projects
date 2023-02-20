

import scrapy

import re
import codecs


class Web3Spider(scrapy.Spider):
    name = "web3"
    start_urls = [
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-schleswig-holstein/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-hamburg/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-niedersachsen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-bremen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-mecklenburg-vorpommern/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-berlin/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-brandenburg/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-sachsen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-sachsen-anhalt/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-thueringen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-nordrhein-westfalen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-rheinland-pfalz/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-hessen/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-baden-wuerttemberg/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-in-bayern/',
        'https://viff-fruehfoerderung.de/fruehfoerderung/fruehfoerderstellen/fruehfoerderstellen-im-saarland/'
        
            ]
    def parse(self, response):
        companies = response.xpath('//div[@class="et_pb_text_inner"]//h2') # select all h2 tags
        for company in companies:
            name = company.xpath("text()").get() # get the text of the h2 tag
            info = company.xpath("following-sibling::p").extract_first() # select the next p tag
            info = info.replace("<p>", "")
            info = info.replace("</p>","")

            parts = info.split("<br>")
            fax = ''
            for l, i in enumerate(parts):
                
                if "@" in i:
                    email = i
                    email = re.sub(r'\\', '', email)
                    email = email.replace("\n","")

                elif len(re.findall(r'\d', i)) >=9 and len(re.findall(r'\d', parts[l+1])) >=9:
                    digits = re.findall(r'\d', i)
                    telefon = ''.join(digits)
                    digits2 = re.findall(r'\d', parts[l+1])
                    fax = ''.join(digits2)
                elif len(re.findall(r'\d', i)) >=9 and len(re.findall(r'\d', parts[l-1])) >=9 == False:
                    digits = re.findall(r'\d', i)
                    telefon = ''.join(digits)
                elif len(re.findall(r'\d', i)) == 5:
                    zip_city_match = re.search(r"(\d{5})\s*(\D+)", i)
                    zip_code = zip_city_match.group(1).strip()
                    # city = zip_city_match.group(2).strip()
                    # zip_code = address.split()[0]

                    # Extract the city name
                    city = ' '.join(i.split()[1:])
                elif len(re.findall(r'\d', i)) >=1 and len(re.findall(r'\d', i)) <=3:
                    address = i
                    address = address.replace("\n","")
                
                









            url = response.url
            yield {
                "company_name": name,
                # "contact_name": contact_name,
                # 'info':i /nfo,
                'address_street': address,
                'address_zipcode': zip_code,
                'address_city':city,
                'contact_phone':telefon,
                'contact_fax':fax,
                'contact_email':email,
                "scrapesource_url":url,

            }
    