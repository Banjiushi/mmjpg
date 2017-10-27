# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 我们需要遍历网页所有套图，拿到套图 url 和标题就可以了
    title = scrapy.Field()
    url = scrapy.Field()
