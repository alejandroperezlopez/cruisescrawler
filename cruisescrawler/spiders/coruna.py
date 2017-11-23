from scrapy.spiders import Spider
from scrapy.selector import Selector
from cruisescrawler.items import Cruise


class CorunaSpider(Spider):
    name = 'coruna'
    start_urls = ['http://www.puertocoruna.com/es/cruceros/cruceros/escalas.html']

    def parse(self, response):
        sel = Selector(response)

        items = sel.xpath('//table[@id="responsive-table-0"]/tbody/tr')

        for item in items:
            cruise = Cruise()

            name = item.xpath('td[2]/text()').extract_first()

            if not name:
                continue

            cruise['name'] = name.strip()

            cruise['date'] = item.xpath('td[1]/text()').extract_first().strip()
            cruise['origin'] = item.xpath('td[5]/text()').extract_first().strip()
            cruise['destination'] = item.xpath('td[6]/text()').extract_first().strip()

            capacity = item.xpath('td[9]/text()')
            if capacity:
                cruise['capacity'] = capacity.extract_first().strip()

            arrival_time = item.xpath('td[7]/text()')
            if arrival_time:
                cruise['arrivalTime'] = arrival_time.extract_first().strip()
            departure_time = item.xpath('td[8]/text()')
            if departure_time:
                cruise['departureTime'] = departure_time.extract_first().strip()
            cruise['port'] = 'CORUNA'

            yield cruise




