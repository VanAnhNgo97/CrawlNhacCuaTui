# -*- coding: utf-8 -*-
import scrapy
import uuid
from tutorial.items import SongItem
class MyMusicSpider(scrapy.Spider):
	name = 'my_music'

	start_urls = [
		#'https://www.nhaccuatui.com/bai-hat/bai-hat-moi.html'
		'https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.1.html'
		#'https://www.nhaccuatui.com/tim-kiem/bai-hat?q=my+tam'
	]

	def parse(self, response):
		for li in response.css("ul.listGenre li"):
			href = li.css("div.info_song a::attr(href)").get()
			yield response.follow(href, self.parse_song)

		# follow pagination links
		for href in response.css('div.box_pageview a.number::attr(href)'):
			yield response.follow(href, self.parse)



	def parse_song(self, response):
		def generate_id():
			song_id = uuid.uuid4()
			return str(song_id)

		def extract_with_css(query):
			return response.css(query).get(default='').strip()

		def extract_singer(query):
			singers = response.css(query).getall()
			rs = ''
			for singer in singers:
				rs = rs + singer
				rs += ", "
			#return response.css(query).getall()
			return rs

		def extract_lyric(query):
			no_lyric = u'Hiện chưa có lời bài hát' #unicode
			sentences = response.css(query).getall()
			lyric = ''
			for st in sentences:
				if no_lyric in st.strip():
					lyric = ""
					break
				else:
					lyric = lyric + st.strip()
					lyric = lyric + " "
			return lyric

		item = SongItem()
		item['title'] = extract_with_css('div.name_title h1::text')
		item['singers'] = extract_singer('div.name_title h2 a.name_singer::text')
		item['lyric'] = extract_lyric('#divLyric *::text')
		yield item

		'''	
		yield {
			#'id' : generate_id(),
			'title': extract_with_css('div.name_title h1::text'),
			'singers' : extract_singer('div.name_title h2 a.name_singer::text'),
			'lyric' : extract_lyric('#divLyric *::text'),
		}
		'''