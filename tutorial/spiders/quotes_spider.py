import scrapy


class QuotesSpider(scrapy.Spider):
	name = "quotes"
	page = 'https://sfbay.craigslist.org'
	def start_requests(self):
		urls = []
		for year in range(2000,2019):
			tmp = 'https://sfbay.craigslist.org/search/cta?max_auto_year=' + str(year) + '&min_auto_year=' + str(year)
			urls.append(tmp)
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for quote in response.xpath('//a[has-class("result-title hdrlnk")]/@href'):
			yield {
			'link': quote.get()
			}

		next_page = response.xpath('//a[has-class("button next")]/@href').get()
		if next_page is not None:
			yield response.follow(self.page + next_page, callback=self.parse)
