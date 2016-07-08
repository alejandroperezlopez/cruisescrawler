from cruisescrawler.spiders.coruna import CorunaSpider
from cruisescrawler.spiders.vigo import VigoSpider
from cruisescrawler.spiders.ferrol import FerrolSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

configure_logging()
runner = CrawlerRunner()


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(FerrolSpider)
    yield runner.crawl(CorunaSpider)
    yield runner.crawl(VigoSpider)
    reactor.stop()


crawl()
reactor.run()