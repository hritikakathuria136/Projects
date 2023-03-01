import scrapy


import re

class Web4Spider(scrapy.Spider):
    name = "web4"
    start_urls = [
        'https://www.dgspj.de/category/sozialpaediatrische-zentren/',
        'https://www.dgspj.de/category/sozialpaediatrische-zentren/page/2/'
        
            ]
    
    def parse(self, response):
        # Extract all the div blocks with class="left_50"
        div_blocks = response.xpath('//div[@class="content_full"]//div[@class="left_50"]')

        # Extract all the div blocks with class="right_50"
        div_blocks2 = response.xpath('//div[@class="content_full"]//div[@class="right_50"]')
        # div_blocks.append(div_blocks2)
        for div in div_blocks:
            # Extract the name of the center
            company_name = div.xpath('h6/text()').get()
            # Extract the address information
            address_lines = div.xpath('p/text()').getall()
            if address_lines:
                if re.search(r"\d+\s*$", address_lines[0]):
                    address_street = address_lines[0]
                    zip_city = address_lines[1]
                else:
                    address_street = address_lines[1]
                    zip_city = address_lines[2]
            
            zip_city_match = re.search(r"(\d{5})\s*(\D+)", zip_city)
            if zip_city_match:
                zip_code = zip_city_match.group(1).strip()
                city = zip_city_match.group(2).strip()
            else:
                zip_code = ""
                city = ""
            phone_number = ""
            phone_line = next((line for line in address_lines if "Tel.:" in line), None)
            if phone_line:
                # Extract the phone number from the line after "TEL"
                phone_number = phone_line.split("Tel.:", maxsplit=1)[1].strip()
            else:
                phone_number = ""
            
            email = div.xpath('p/a/text()').get()
            company_notes = div.xpath('p/strong[1]/text()').get()
            fax = next((line for line in address_lines if "Fax:" in line), None)
            if fax:
                # Extract the phone number from the line after "TEL"
                fax_l= fax.split("Fax:", maxsplit=1)[1].strip()
            else:
                fax_l = ""
            homepage_link = div.xpath('.//a[@target="_blank"]/@href').get()
            scrapesource_url = 'https://www.dgspj.de/category/sozialpaediatrische-zentren/'
            # Yield the extracted data as a dictionary
            yield {
                'company_name': company_name,
                'address_street': address_street,
                'address_zip':zip_code,
                'address_city':city,
                'contact_phone': phone_number,
                'contact_fax':fax_l,
                'contact_email': email,
                'contact_website_url':homepage_link,
                'company_notes':company_notes,
                'scrapesource_url':scrapesource_url
            }
        for div in div_blocks2:
            # Extract the name of the center
            company_name = div.xpath('h6/text()').get()
            # Extract the address information
            address_lines = div.xpath('p/text()').getall()
            if address_lines:
                if re.search(r"\d+\s*$", address_lines[0]):
                    address_street = address_lines[0]
                    zip_city = address_lines[1]
                else:
                    address_street = address_lines[1]
                    zip_city = address_lines[2]
            
            zip_city_match = re.search(r"(\d{5})\s*(\D+)", zip_city)
            if zip_city_match:
                zip_code = zip_city_match.group(1).strip()
                city = zip_city_match.group(2).strip()
            else:
                zip_code = ""
                city = ""
            phone_number = ""
            phone_line = next((line for line in address_lines if "Tel.:" in line), None)
            if phone_line:
                # Extract the phone number from the line after "TEL"
                phone_number = phone_line.split("Tel.:", maxsplit=1)[1].strip()
            else:
                phone_number = ""
            
            email = div.xpath('p/a/text()').get()
            company_notes = div.xpath('p/strong[1]/text()').get()
            fax = next((line for line in address_lines if "Fax:" in line), None)
            if fax:
                # Extract the phone number from the line after "TEL"
                fax_l= fax.split("Fax:", maxsplit=1)[1].strip()
            else:
                fax_l = ""
            homepage_link = div.xpath('.//a[@target="_blank"]/@href').get()
            scrapesource_url = 'https://www.dgspj.de/category/sozialpaediatrische-zentren/'
            # Yield the extracted data as a dictionary
            yield {
                'company_name': company_name,
                'address_street': address_street,
                'address_zip':zip_code,
                'address_city':city,
                'contact_phone': phone_number,
                'contact_fax':fax_l,
                'contact_email': email,
                'contact_website_url':homepage_link,
                'company_notes':company_notes,
                'scrapesource_url':scrapesource_url
            }