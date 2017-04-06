# -*- coding: utf-8 -*-
import re
import json
import scrapy

from scrapy.selector import Selector

from images.items import ImagesItem

class ImagesSpider(scrapy.Spider):
	name = "images"
	allowed_domains = ["chanyouji.com"]
	start_urls = [
		"http://www.chanyouji.com/trips/544896"
		]

	#parse data to items using XPath 
	def parse(self,response):
		items = []# to gennerate json style
		sel = Selector(response)
		sites = sel.xpath('//div[contains(@data-type,"photo")]')
		site1 = sites.xpath('div[starts-with(@class,"note-content")]/figure')
		site2 = site1.xpath('figcaption')
		site3 = sel.xpath('//div[contains(@data-type,"node")]')
		index1 = 0 # to clean the desc
		index2 = 0 # to add album_id
#		index3 = 0
		for index in range(len(sites)):
			item = ImagesItem()
			item['path'] = sel.xpath('//html').re(r'"src":"(.*?)"')[index]
			item['photo'] = sel.xpath('//html').re(r'"src":"http://(.*?)"')[index]
			item['photo_id'] = sel.xpath('//div[contains(@data-type,"photo")]/@id').extract()[index]
			item['datetaken'] = sel.xpath('//div[contains(@data-type,"photo")]/div[@class="note-footer"]/time/@datetime').extract()[index]
			#generate desc item
			if bool(site1[index].xpath('figcaption').extract())==True:
					item['desc'] = site2.xpath('p/text()').extract()[index1]
					index1 =index1+1
			#generate album_id item
			if sites[index].re(r'data-group="(...).*?"') == site3[index2].re(r'data-group="(.*?)"'):
				item['album_id'] = site3[index2].xpath('@id').extract()
			else:
				index2 = index2+1
				item['album_id'] = site3[index2].xpath('@id').extract()
			items.append(item)
		return items
			




