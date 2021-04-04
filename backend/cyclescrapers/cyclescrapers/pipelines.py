# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class CyclescrapersPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='',
            dbname='cyclodb'
        )
        self.cur = self.connection.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cyclo_items (
                name varchar(255),
                price varchar(255),
                retailer varchar(255),
                url varchar(255)
            )
        """)
        self.connection.commit()


    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()


    def process_item(self, item, spider):
        self.cur.execute("insert into cyclo_items(name, price, retailer, url) values(%s, %s, %s, %s)", (item['name'], item['price'], item['retailer'], item['url']))
        self.connection.commit()
        print(item['name'])
        print(item['price'])
        print(item['url'])
        print(item['retailer'])
        return item
