# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class JolseSpider(CrawlSpider):
    name = "jolse_spider"
    allowed_domains = ["jolse.com"]
    start_urls = (
        'http://www.jolse.com/products/SKINCARE/26',
    )

    rules = (
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
    Rule(LinkExtractor(allow=(r'\/product\/detail\.html'))),
    Rule(LinkExtractor(allow=(r'\/product\/(?!detail)(?!list)')),callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
