import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from cruisescrawler.items import Cruise


class VigoSpider(Spider):
    name = 'vigo'
    start_urls = ['http://www.apvigo.com/control.php?sph=a_iap=1110%%p_rpp=1']

    def parse(self, response):
        sel = Selector(response)

        items = sel.xpath('//div[@id="contenidos"]/table[@class="tabla"]/'
                          'tr[contains(@class, "fila1") or contains(@class, "fila2")]')
        for item in items:
            cruise = Cruise()

            name = item.xpath('td[2]/span/text()').extract_first()

            if not name:
                continue

            cruise['name'] = name.strip()

            cruise['date'] = item.xpath('td[1]/span/text()').extract_first().strip()
            cruise['origin'] = item.xpath('td[6]/span/text()').extract_first().strip()
            cruise['destination'] = item.xpath('td[7]/span/text()').extract_first().strip()
            cruise['arrivalTime'] = item.xpath('td[4]/span/text()').extract_first().strip()
            cruise['departureTime'] = item.xpath('td[5]/span/text()').extract_first().strip()
            cruise['port'] = 'VIGO'

            yield cruise




