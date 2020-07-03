import sys

import validators
from scrapy.crawler import CrawlerProcess

from rgr_scrapy.spiders.rgr_scrapy import PhonesSpider


urls = [url.strip() for url in list(sys.stdin) if url and validators.url(url)]

print ("We'll crawler these URLś for you: {}".format(urls))

process = CrawlerProcess({
'USER_AGENT:':'Mozilla / 4.0 (compatible; MSIE 7.0; Windows NT 5.1',
'FEED_FORMAT': 'json',
'FEED_URI': 'result.json'
})

process.crawl(PhonesSpider,urls = urls)
process.start()
