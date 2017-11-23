from scrapy.spiders import Spider
from scrapy.selector import Selector
from cruisescrawler.items import Cruise


class VigoSpider(Spider):
    name = 'vigo'
    start_urls = ['https://www.apvigo.es/paginas/prevision_cruceros']

    def parse(self, response):
        sel = Selector(response)

        items = sel.xpath('//div[@class="listado"]/table[@class="listado responsive"]/tbody/tr')
        for item in items:
            cruise = Cruise()

            name = item.xpath('td[@class="buque"]/text()').extract_first()

            if not name:
                continue

            cruise['name'] = name.strip()

            cruise['date'] = item.xpath('td[@class="fecha llegada"]/text()').extract_first().strip()
            cruise['origin'] = item.xpath('td[@class="procedencia"]/text()').extract_first().strip()
            cruise['destination'] = item.xpath('td[@class="destino"]/text()').extract_first().strip()
            cruise['arrivalTime'] = item.xpath('td[@class="hora horaLlegada"]/text()').extract_first().strip()
            cruise['departureTime'] = item.xpath('td[@class="hora horaSalida"]/text()').extract_first().strip()

            cruise['port'] = 'VIGO'

            yield cruise




