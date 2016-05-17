# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cruise(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    name = scrapy.Field()
    origin = scrapy.Field()
    destination = scrapy.Field()
    capacity = scrapy.Field()
    arrivalTime = scrapy.Field()
    departureTime = scrapy.Field()
    port = scrapy.Field()
