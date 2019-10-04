# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Selecting 'CrawlSpider' - as this is designed to follow links
# functionality can be overrided and customised as required
class BooksSpider(CrawlSpider):
    # Crawler assigned the name 'links'
    name = 'links'
    allowed_domains = [
        'thebookpeople.co.uk',
        'bookswagon.com',
        'thriftbooks.com',
        'jainbookagency.com',
        'highwaybooks.ca',
        'bookcity.ca',
        'onlineinnovations.com/websites',
        'en.wikipedia.org/wiki/Mathematics',
        'guru99.com',
        'gizmodo.com',
        'crocodiletoys.com'
    ]


    start_urls = [
        # 'https://thebookpeople.co.uk/'
        # 'https://bookswagon.com/'
        # 'https://thriftbooks.com/'
        # 'https://jainbookagency.com/'
        # 'http://highwaybooks.ca/'
        # 'http://bookcity.ca/'
        # 'https://on
        # 'lineinnovations.com/websites'
        # 'https://en.wikipedia.org/wiki/Mathematics'
        # 'https://guru99.com'
        # 'https://gizmodo.com'
        'https://crocodiletoys.com/'
    ]

    # set one or more rules - for example, to filter out social media pages, such as Facebook, Linkedin, Twitter, etc;
    # or to only include specific keywords
    # rules = (Rule(LinkExtractor(allow=('honey'), deny_domains=('google.com')), callback='parse_page',follow=False), )
    rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=True), )

    # yield results for output
    def parse_page(self, response):
        yield {
            'URL': response.url
            }
