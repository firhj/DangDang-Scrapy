# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl

class DangdangPipeline(object):
    def __init__(self):
        self.wb =openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司', '职位', '地址', '招聘信息'])
        self.ws.append(['书名', '价格'])
    def process_item(self, item, spider):
        line = [item['name'],item['price']]
        print (line)
        self.ws.append(line)
        return item
    def close_spider(self, spider):
        self.wb.save('./yingxiang.xlsx')
        self.wb.close()
