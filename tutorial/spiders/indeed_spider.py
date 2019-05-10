import scrapy


class QuotesSpider(scrapy.Spider):
	name = "indeed"
	page = 'https://www.indeed.com/jobs?q=data+scientist&sort=date'
	def start_requests(self):
		urls = ['https://www.indeed.com/jobs?q=data+scientist&sort=date']
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		yield {
		'Full time': int(response.xpath('//a[contains(@title, "Full-time")]/span[2]/text()').extract()[0][1:-1]),
		'Part time': int(response.xpath('//a[contains(@title, "Part-time")]/span[2]/text()').extract()[0][1:-1])
		}


