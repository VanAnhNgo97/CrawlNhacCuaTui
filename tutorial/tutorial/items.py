# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    singers = scrapy.Field()
    lyric = scrapy.Field()
    #link = scrapy.Field()
    '''
    title = scrapy.Field()
  	singers = scrapy.Field()
  	lyric = scrapy.Field()
	'''