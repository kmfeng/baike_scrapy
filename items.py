# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class baikeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    description = Field()
#    linkwords = Field()
    url = Field()


class baikeSiteItem(Item):
#    name = Field()
    url = Field()
