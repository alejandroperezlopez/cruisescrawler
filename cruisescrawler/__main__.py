from .spiders.coruna import CorunaSpider
from .spiders.vigo import VigoSpider
from .spiders.ferrol import FerrolSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

configure_logging()
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(FerrolSpider)
    yield runner.crawl(CorunaSpider)
    yield runner.crawl(VigoSpider)
    reactor.stop()


crawl()
reactor.run()

