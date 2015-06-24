from scrapy.spiders 		import Spider
from scrapy.selector 		import Selector
from nettuts.items		import NettutsItem
from scrapy.http		import Request

class MySpider(Spider):
	name 		= "nettuts"
	allowed_domains	= ["uthh.edu.mx"]
	start_urls	= ["http://uthh.edu.mx/2015/?val=cHJlbnNhLnBocA==&M=NDg=&a=MjAxNQ=="]

	def parse(self, response):
		hxs 	= Selector(response)
		selectors 	= hxs.xpath('//div[@class="grid_2"]')
		for sel in selectors:
			item = NettutsItem()
			item["title"] = sel.xpath('a/div[@class="titulo"]/text()').extract()
			item["link"] = sel.xpath('a/@href').extract()			
			
			des = sel.xpath('a/div[@class="texto"]/p/text()').extract()
			if not des:
				des = sel.xpath('a/div[@class="texto"]/text()').extract()

			item["desc"] = des
			yield item