import scrapy

import re
import codecs

def clean_and_encode(text):
    # Remove non-standard letters
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Check if the text is already encoded
    if isinstance(text, bytes):
        return text
    try:
        # Encode the text as UTF-8
        return text.encode("utf-8")
    except UnicodeEncodeError as e:
        # Print the error message
        print("Error:", e)
        return None
def str_join(list):
    company_note = ''.join(",", list)
    return company_note
class NamesSpider(scrapy.Spider):
    name = "names"
    start_urls = [
        'https://xn--frhfrderstellen-ctb3h.de/fruehfoerderstellenfinder/',
    ]
    
    def parse(self, response):
        for item in self.parse_item(response):
            yield item
            # Find the link to the next page
        next_page = response.css("ul.f3-widget-paginator li.next a[rel='next']::attr(href)").get()
        if next_page is not None:
            # Make a request to the next page and pass it back to the parse method
            yield response.follow(next_page, self.parse)
    
    def parse_item(self, response):
        # Extract the data for each item on the current page
        # response.replace(encoding = 'utf-8')
        # response = response.encode('iso-8859-1')
        # response = response.decode('utf-8')
        columns = response.css('div[class="listview"] div[class="list row"]')
        for col in columns:
            # Get the required text from element.
            company_name= col.css('div[class="title fn org p-name"]::text').extract_first()
           
            address_zip= col.css('span[class="postal-code p-postal-code"]::text').get()
            address_street= col.css('div[class="street-address p-street-address"]::text').get()                
            address_city= col.css('span[class="locality p-locality"]::text').get()
            contact_email= col.css('div.detail a span.email::text').get()
            contact_phone= col.css('div.detail span.tel::text').get()
            contact_fax= col.css('div.detail span[itemprop="faxNumber"]::text').get()
            contact_website_url=col.css('.detail[title="Webseite"] a span.url::text').get()
            company_organization= col.css('div.detail[title="Träger"] span[itemprop="parentOrganization"]::text').get()
            areaServed= col.css('.detail[title="Einzugsbereich"] span[itemprop="areaServed"]::text').get()
            company_servicetype_mobility= col.css('div.detail[title = "Organisationsform"] span::text').get()
            company_notes= ' '.join(col.css('div.detail span.note p::text').getall())
            # scrapesource_url=response.css("ul.f3-widget-paginator li.next a[rel='next']::attr(href)").get()
            scrapesource_url = 'https://xn--frhfrderstellen-ctb3h.de/fruehfoerderstellenfinder/'
            yield {
                "company_name": company_name,
                'address_zip': address_zip,
                'address_street': address_street,
                'address_city': address_city,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'contact_fax': contact_fax,
                'contact_website_url':contact_website_url,
                'company_organization': company_organization,
                'areaServed':areaServed,
                'company_servicetype_mobility': company_servicetype_mobility,
                'company_notes': company_notes,
                'scrapesource_url':scrapesource_url
            }
            