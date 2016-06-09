import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from cruisescrawler.items import Cruise


class FerrolSpider(Spider):
    name = 'ferrol'
    start_urls = ['http://www.apfsc.com/castellano/puerto_ciudad/cruceros.html']

    def parse(self, response):
        sel = Selector(response)

        items = sel.xpath('//table[@align="center"]/tbody/tr')

        for item in items:
            cruise = Cruise()

            cruise['name'] = item.xpath('td[2]/text()').extract_first()

            if not cruise['name']:
                continue

            cruise['date'] = item.xpath('td[1]/text()').extract_first()

            cruise['origin'] = item.xpath('td[5]/text()').extract_first()
            cruise['destination'] = item.xpath('td[6]/text()').extract_first()
            cruise['capacity'] = item.xpath('td[4]/text()').extract_first()
            cruise['arrivalTime'] = item.xpath('td[7]/text()').extract_first()
            cruise['departureTime'] = item.xpath('td[8]/text()').extract_first()
            cruise['port'] = 'FERROL'

            yield cruise




