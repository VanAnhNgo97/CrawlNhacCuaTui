# -*- coding: utf-8 -*-
import scrapy
class MP3Spider(scrapy.Spider):
	name = 'my_mp3_file'

	start_urls = [
		#'https://www.nhaccuatui.com/bai-hat/bai-hat-moi.html'
		'https://www.nhaccuatui.com/tim-kiem/bai-hat?q=my+tam'
	]

	def parse(self, response):
		for li in response.css("ul.sn_search_returns_list_song li"):
			href = li.css("div.box_info h3.title_song a::attr(href)").get()
			yield response.follow(href, self.parse_song)

		# follow pagination links
		for href in response.css('div.box_pageview a.number::attr(href)'):
			yield response.follow(href, self.parse)