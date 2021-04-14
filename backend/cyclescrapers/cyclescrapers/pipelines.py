# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class CyclescrapersPipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect( ################################################needs to be moved to config or env
            host='localhost',
            user='postgres',
            password='secret',
            dbname='cyclodb'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cyclo_retailer (
                name        varchar(255) PRIMARY KEY,
                link        varchar(255)
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cyclo_product (
                link        varchar(255) PRIMARY KEY,
                name        varchar(255),
                price       varchar(255)
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sells (
                retailer    varchar(255),
                product     varchar(255)
            )
        """)
        self.conn.commit()


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()


    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO cyclo_product(link, name, price) values(%s, %s, %s)
        """, (item['url'], item['name'], item['price'])
        )
        self.cur.execute("""
            INSERT INTO cyclo_retailer(name, link) values(%s, %s)
        """, (item['retailer'], item['url'])
        )
        self.cur.execute("""
            INSERT INTO sells(retailer, product) values(%s, %s)
        """, (item['retailer'], item['name'])
        )
        self.conn.commit()
        print(item['name'])
        print(item['price'])
        print(item['url'])
        print(item['retailer'])
        return item
