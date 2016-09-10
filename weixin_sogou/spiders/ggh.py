#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from weixin_sogou.items import WeixinSogouItem
import scrapy

class HuxiuSpider(scrapy.Spider):
    name = "weixin"
    allowed_domains = ["sogou.com"]
    start_urls = [
        "http://weixin.sogou.com/"
    ]

    def parse(self, response):
        for sel in response.css('h4').xpath('./a/text()'):
            item = WeixinSogouItem()
            item['title'] = sel.css('h4').xpath('./a/text()').extract()
            item['link'] = sel.css('h4').xpath('./a/@href').extract()
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('//div[@class="pos-wxrw"]//@title').extract()
            print(item['title'],item['link'],item['desc'])