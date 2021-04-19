import requests
import html5lib
from bs4 import BeautifulSoup

def jenson_scrape(search_term: str):
    try:
        print(search_term)
        r = requests.get('https://www.jensonusa.com/search?q=' + search_term)
        # print(r.text)
        soup = BeautifulSoup(r.text, features='html5lib')
        # print(soup.prettify())
        names = soup.select('a[class*=product-name]')
        prices = soup.select('div[class*=product-price-saleprice]')
        item_urls = soup.select('a[class*=product-name]')
        # for url in item_urls:
        #     print(url['href'])

        item = {}
        item['name'] = names[0].text.strip()
        item['price'] = prices[0].text.strip()
        item['retailer'] = 'Jenson USA'
        item['url'] = 'https://www.jensonusa.com' + item_urls[0]['href']
        print(item)
        return item
        # print(names) 
    except:
        return {}


def bikebling_scrape(search_term: str):
    try:
        print(search_term)
        r = requests.get("https://www.bikebling.com/SearchResults.asp?Search=" + search_term)
        # print(r.text)
        soup = BeautifulSoup(r.text, features='html5lib')
        # print(soup.prettify())
        names = soup.select('a[class*=v-product__title]')
        prices = soup.select('div[class*=product_productprice]')
        item_urls = soup.select('a[class*=v-product__title]')
        # for url in item_urls:
        #     print(url['href'])

        item = {}
        item['name'] = names[0].text.strip()
        item['price'] = prices[0].text.strip()
        item['retailer'] = 'Bike Bling'
        item['url'] = item_urls[0]['href']
        print(item)
        return item
    except:
        return {}

def competitive_scrape(search_term: str):
    try:
        print(search_term)
        r = requests.get("https://www.competitivecyclist.com/Store/catalog/search.jsp?s=u&q=" + search_term)
        # print(r.text)
        soup = BeautifulSoup(r.text, features='html5lib')
        # print(soup.prettify())
        names = soup.select('span[class*=ui-pl-name-title]')
        prices = soup.select('span[class*=js-pl-price]')
        item_urls = soup.select('a[class*=ui-pl-link]')
        # for url in item_urls:
        #     print(url['href'])

        item = {}
        item['name'] = names[0].text.strip()
        item['price'] = prices[0].text.strip()
        item['retailer'] = 'Competitive Cyclist'
        item['url'] = 'https://www.competitivecyclist.com' + item_urls[0]['href']
        print(item)
        return item
    except:
        return {}

def chainreaction_scraper(search_term: str):
    try:
        print(search_term)
        r = requests.get("https://www.chainreactioncycles.com/us/en/s?q=" + search_term)
        # print(r.text)
        soup = BeautifulSoup(r.text, features='html5lib')
        # print(soup.prettify())
        names = soup.select('li[class*=description]')
        prices = soup.select('li[class*=fromamt]')
        item_urls = soup.select('li[class*=description]')
        # for url in item_urls:
        #     print(url['href'])

        item = {}
        item['name'] = names[0].text.strip()
        item['price'] = prices[0].text.strip().split(u'\xa0')[0]
        item['retailer'] = 'Chain Reaction Cycles'
        item['url'] = 'https://www.chainreactioncycles.com' + item_urls[0].find('a')['href']
        print(item)
        return item
    except:
        return {}

def backcountry_scraper(search_term: str):
    try:
        print(search_term)
        r = requests.get("https://www.backcountry.com/Store/catalog/search.jsp?s=u&q=" + search_term)
        # print(r.text)
        soup = BeautifulSoup(r.text, features='html5lib')
        # print(soup.prettify())
        names = soup.select('span[class*=ui-pl-name-title]')
        prices = soup.select('span[class*=js-pl-price]')
        item_urls = soup.select('a[class*=ui-pl-link]')
        # for url in item_urls:
        #     print(url['href'])

        item = {}
        item['name'] = names[0].text.strip()
        item['price'] = prices[0].text.strip()
        item['retailer'] = 'Backcountry'
        item['url'] = 'https://www.backcountry.com' + item_urls[0]['href']
        print(item)
        return item
    except:
        return {}

def run_scrapers(search_term: str):
    data = []
    data.append(jenson_scrape(search_term))
    data.append(bikebling_scrape(search_term))
    data.append(competitive_scrape(search_term))
    data.append(chainreaction_scraper(search_term))
    data.append(backcountry_scraper(search_term))
    return data

# run_scrapers('maxxis+minion')

