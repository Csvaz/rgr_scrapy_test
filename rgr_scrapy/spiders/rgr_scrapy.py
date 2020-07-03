import re
import logging
from urllib.parse import urlparse

import scrapy


logging.getLogger('scrapy').propagate = False


class PhonesSpider(scrapy.Spider):
    name = "phones"
    urls = []

   
    def start_requests(self):
        
        for url in self.urls:
            self.log("Scrapping... " + url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       
        info_site = {'logo':[],'phones':[], 'website':[]}
        
    
        
        logo_xpath = ['//img/@src[contains(., "logo")]',
                      '//img[contains(@class,"logo")]/@src',
                      '//img[contains(@class,"icon")]/@src',
                      '//img/@src[contains(., "Logo")]']

        url_data = urlparse(response.url)
        domain_url = "{}://{}".format(url_data.scheme, url_data.netloc)


        for xpath in logo_xpath:
            for image in  response.xpath(xpath).getall():
                if image:
                    if image.startswith("http"):
                        info_site['logo'].append(image)
                    else:
                        if image.startswith("//"):
                            info_site['logo'].append(
                                '{}:{}'.format(url_data.scheme,image))
                        else:
                            info_site['logo'].append(
                                '{}{}'.format(domain_url,image))
                

        re.purge()
        regex = ">(\(?\+?[0-9]+\)?)?([0-9_\- \(\)\/.]+)<"
        phone_regex= re.compile(regex)
        
        body = response.xpath('//body').extract_first()
        
        phones = [phone for phone in set(phone_regex.findall(body)) if phone]       
        
        char_to_remove = "-/\.  "
        pattern_phone = "[" + char_to_remove + "]"     

        for phone in phones:
            first, second = phone
            if first:
                info_site['phones'].append(
                    re.sub(pattern_phone," ","".join(phone).strip()))


        info_site['website'].append(response.url)
        
        yield info_site