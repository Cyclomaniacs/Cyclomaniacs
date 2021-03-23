from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def run_scrapers(search_term: str):

    search_term = '_'.join(search_term.split(' ')) # format correctly for command line arg parsing
    setting = get_project_settings()
    spider_loader = CrawlerProcess._get_spider_loader(setting)

    process = CrawlerProcess(setting)
    for spider_name in spider_loader.list():
        print ("Running spider %s" % (spider_name))
        process.crawl(spider_name, item='dog') 
    process.start()