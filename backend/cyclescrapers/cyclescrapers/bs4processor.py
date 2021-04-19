def create_table():
    self.conn = psycopg2.connect( ################################################needs to be moved to config or env
        host='localhost',
        user='postgres',
        password='secret',
        dbname='cyclodb'
    )
    self.cur = self.conn.cursor()

    self.cur.execute("""
        CREATE TABLE IF NOT EXISTS cyclo_product (
            link        varchar(255) PRIMARY KEY,
            name        varchar(255),
            price       varchar(255),
            retailer    varchar(255)
        )
    """)

    self.conn.commit()



def process_item(self, item, spider):
    self.cur.execute("""
        INSERT INTO cyclo_product(link, name, price, retailer) values(%s, %s, %s, %s)
    """, (item['url'], item['name'], item['price'], item['retailer'])
    )

    # self.cur.execute("""
    #     INSERT INTO cyclo_retailer(name, link) values(%s, %s)
    # """, (item['retailer'], item['url'])
    # )
    # self.cur.execute("""
    #     INSERT INTO sells(retailer, product) values(%s, %s)
    # """, (item['retailer'], item['name'])
    # )
    self.conn.commit()
    print(item['name'])
    print(item['price'])
    print(item['url'])
    print(item['retailer'])
    return item