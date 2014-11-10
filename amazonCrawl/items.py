# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazoncrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
   # categoryURL = scrapy.Field()
    productImage = scrapy.Field()
    productName = scrapy.Field()
    productPrice = scrapy.Field()
    productOrigin = scrapy.Field()
    productUrl = scrapy.Field()


    
