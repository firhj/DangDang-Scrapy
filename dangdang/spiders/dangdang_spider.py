# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import DangdangItem

class DangdangSpiderSpider(scrapy.Spider):
    name = 'dangdang_spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%D2%BD%D1%A7%D3%B0%CF%F1&act=input&page_index=1']


    def parse(self, response):
        books_info=response.xpath('//ul[@class="bigimg"]/li')
        for book in books_info:
            name = book.xpath('./a/@title').get(default='')
            price_str = book.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').get(default='')
            price=float(price_str[1:])
            item=DangdangItem()
            item['name'] = name
            item['price'] = price
            yield item
        page_num=1
        while page_num!=5:
            new_page_url='http://search.dangdang.com/?key=%D6%D0%D2%BD&act=input&page_index={}'.format(page_num)
            page_num = page_num + 1
            yield scrapy.Request(new_page_url,callback=self.parse)



