# -*- coding: utf-8 -*-
import scrapy
class MyMusicSpider(scrapy.Spider):
	name = 'my_singer'

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



	def parse_song(self, response):
		def extract_with_css(query):
			return response.css(query).get(default='').strip()

		def extract_singer(query):
			return response.css(query).getall()

		def extract_lyric(query):
			sentences = response.css(query).getall()
			lyric = ''
			for st in sentences:
				lyric = lyric + st.strip()
				lyric = lyric + " "
			return lyric


		yield {
			'title': extract_with_css('div.name_title h1::text'),
			'singers' : extract_singer('div.name_title h2 a.name_singer::text'),
			'lyric' : extract_lyric('#divLyric *::text'),
		}