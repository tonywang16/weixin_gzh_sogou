#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from weixin_sogou.items import WeixinSogouItem
import scrapy

class WeixinSpider(scrapy.Spider):
    name = "weixin"
    allowed_domains = ["sogou.com","mp.weixin.qq.com"]
    start_urls = [
        "http://weixin.sogou.com/"

    ]

    def parse(self, response):
        #print response.css('h4').xpath('./a/text()').extract()[0]
        for  sel in response.xpath('//*[@id="pc_0_subd"]/li'):
        #for sel in response.xpath('//*[@id="pc_0_subd"]/li//div[@class="wx-news-info2"]/h4/a'):
            #print sel.xpath('./div[@class="wx-news-info2"]/h4/a/text()').extract_first()
            item = WeixinSogouItem()
            #item['title'] = sel.xpath('//div[@class="wx-news-info2"]/h4/a/text()')[0].extract()
            item['title'] = sel.xpath('./div[@class="wx-news-info2"]/h4/a/text()').extract_first()
            #print sel.xpath('//li/div/h4/a/text()')[0].extract()
            item['link'] = sel.xpath('./div[@class="wx-news-info2"]/a/@href').extract_first()
            #url = response.urljoin(item['link'])
            url = response.urljoin(item['link'])
            item['desc'] = sel.xpath('./div[@class="wx-news-info2"]/a/text()').extract_first()
            item['author'] = sel.xpath('./div[@class="pos-wxrw"]/a/p/@title').extract_first()
            print item['title']
            #request = scrapy.Request(url, callback=self.parse_article)
            #request.meta['item'] = item
            #return request
            #print (item['title'],item['author'],item['link'])
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        #detail = response.xpath('//div[@class="rich_media_area_primary"]').extract_first()
        #item = response.meta['item']
        print 'Im here'
        item = WeixinSogouItem()
        item['link'] = response.url
        #item['title'] = detail.xpath('h1/text()')[0].extract()
        item['body'] =  response.xpath('//div[@class="rich_media_area_primary"]').extract_first()
        #print response.xpath('//div[@class="rich_media_area_primary"]').extract_first()
        #item['posttime'] = detail.xpath(
        #    'div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
        #print item['body']
        yield item
