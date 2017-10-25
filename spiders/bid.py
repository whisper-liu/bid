# -*- coding:utf-8 -*-

import scrapy
from bid.items import BidItem
import re
class bid(scrapy.Spider):
    name = 'bid'
    start_urls = []
    nums = 5
    for i in range(1,nums):
        start_urls.append('http://www.bgpc.gov.cn/defaults/news/news/page/' + str(i) + '%2Ftid%2F2')
        print(start_urls)
    def parse(self, response):
        item = BidItem()
#        print(response.body)/html/body/div[1]/div/div[2]/div[2]/div/div[2]/li[1]/a
        name = response.xpath('//li/a/@title').extract()
        print(name)
        url = response.xpath('//li/a[@title]/@href').extract()
        print(url)
        dat = response.xpath('//li/span/text()').extract()
#        print(dat)
        for n,u,d in zip(name,url,dat):
            item['name'] = n
            item['url'] = 'http://www.bgpc.gov.cn'+u
            item['dat'] = d
            yield item