# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BidItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    dat = scrapy.Field()
    url = scrapy.Field()
