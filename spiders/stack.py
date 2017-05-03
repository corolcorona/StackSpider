# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.http import Request
from StackSpider.items import StackspiderItem
import re

class StackSpider(RedisSpider):
    name = "stack"
    #allowed_domains = ["stackoverflow.com"]
    start_urls = ['http://stackoverflow.com/questions']

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')
        
        for question in questions:
            item = StackspiderItem()
            item['title'] = question.xpath('h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['link'] = question.xpath('h3/a[@class="question-hyperlink"]/@href').extract()[0]
            yield item


