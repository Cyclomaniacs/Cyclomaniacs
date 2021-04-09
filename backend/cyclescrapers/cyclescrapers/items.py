# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CyclescrapersItem(scrapy.Item):

    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    retailer = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
