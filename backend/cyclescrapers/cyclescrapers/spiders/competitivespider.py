import scrapy
from cyclescrapers.items import CyclescrapersItem

class CompetitiveSpider(scrapy.Spider):
    name = 'competitive'
    
    # def __init__(self, item='', **kwargs):
    #     clean_item = item.split()
    #     clean_item = '+'.join(clean_item)
    #     self.start_urls = [f'https://www.jensonusa.com/search?q={clean_item}']  # py36
    #     super().__init__(**kwargs)  # python3


    def start_requests(self):
        print(self.item)
        clean_item = self.item.split('_') # must pass spaced name as underscores
        clean_item = '+'.join(clean_item)
        yield scrapy.Request("https://www.competitivecyclist.com/Store/catalog/search.jsp?s=u&q=" + clean_item)



    def parse(self, response):
        CycleItem = CyclescrapersItem()
        
        names = response.css('span[class*=ui-pl-name-title]::text').getall()
        prices = response.css('span[class*=js-pl-price]::text').getall()
        item_urls = response.css('a[class*=ui-pl-link]::attr(href)').getall()

        CycleItem['name'] = names[0].strip()
        CycleItem['price'] = prices[0].strip()
        CycleItem['url'] = 'https://www.competitivecyclist.com' + item_urls[0] # item url is only extension at end of base url
        CycleItem['retailer'] = 'Competitive Cyclist'
        #TODO maybe return the top three instead of just the top one
        # for name, price in zip(names, prices):
        #     print(name.strip())
        #     print(price.strip())

        yield CycleItem



