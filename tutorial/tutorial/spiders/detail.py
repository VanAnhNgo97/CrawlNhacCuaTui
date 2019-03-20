import scrapy
class DetailSpider(scrapy.Spider):
	name = 'detail'

	start_urls = [
		'http://quotes.toscrape.com/'
	]

	def parse(self, response):
		for quote in response.css("div.quote"):
			href = quote.css(".author + a::attr(href)'")
			#author_detail  = yield response.follow(href, self.parse_author)
			yield {
				'text' : quote.xpath("//span[@class='text']/text()").get(),
 				'author' : quote.xpath("//small[@class='author']/text()").get(),
 				#'tags': quote.xpath("//div[@class='tags'/a[@class='tag']/text()").getall()
 				'tags' : quote.css("div.tags a.tag::text").getall(),
 				'author_detail' : author_detail,
			}

	

