def create_table(conn, cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cyclo_retailer (
            name        varchar(255) PRIMARY KEY,
            link        varchar(255)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS cyclo_product (
            link        varchar(255) PRIMARY KEY,
            name        varchar(255),
            price       varchar(255)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sells (
            retailer    varchar(255),
            product     varchar(255)
        )
    """)

    conn.commit()


def insert_item(conn, cur, item):
    cur.execute("""
        INSERT INTO cyclo_product(link, name, price) values(%s, %s, %s)
    """, (item['url'], item['name'], item['price']))

    cur.execute("""
        INSERT INTO cyclo_retailer(name, link) values(%s, %s)
    """, (item['retailer'], item['url']))

    cur.execute("""
        INSERT INTO sells(retailer, product) values(%s, %s)
    """, (item['retailer'], item['name']))

    conn.commit()


def default_retrieve_items(conn, cur):
    cur.execute("""
        WITH
            a AS (SELECT * FROM sells),
            b AS (SELECT * FROM cyclo_product)

        SELECT link, name, price, retailer FROM (a RIGHT OUTER JOIN b ON a.product = b.name)
    """)

    conn.commit()


def drop_all_tables(conn, cur):
    cur.execute("""
        DROP TABLE cyclo_retailer
    """)

    cur.execute("""
        DROP TABLE cyclo_product
    """)

    cur.execute("""
        DROP TABLE sells
    """)

    conn.commit()