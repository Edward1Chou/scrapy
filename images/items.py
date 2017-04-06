# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class ImagesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	datetaken = scrapy.Field()
	photo = scrapy.Field()
	path = scrapy.Field()
	desc = scrapy.Field()
	photo_id = scrapy.Field()
	album_id = scrapy.Field()
