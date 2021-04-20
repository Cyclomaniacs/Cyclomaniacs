import psycopg2
from flask import jsonify
from model.bs4scrapers import run_scrapers
from model.db_manip import *

class Search:
    ##################################################PRIVATE  METHODS##################################################
    # __initDB(self):
    #   Private database connection initializer that checks if connection has been established. If connection fails,
    #   throw an exception.
    def __initDB(self):
        try:
            self.conn = psycopg2.connect(  ###########################################needs to be moved to config or env
                host='localhost',
                user='postgres',
                password='secret',
                dbname='cyclodb'
            )
        except Exception as err:
            print(err)
            self.conn = None

    # __initCursor(self):
    #   Private cursor initializer that checks if connection exists. If there is no connection, throw an exception.
    def __initCursor(self):
        try:
            if self.conn is not None:
                self.cur = self.conn.cursor()
            else:
                raise Exception('Tried to retrieve cursor from null database')
        except Exception as err:
            print(err)
            self.cur = None


    def __initTable(self):
        try:
            if self.conn is not None:
                self.cur = self.conn.cursor()

                create_table(self.conn, self.cur)

                # self.cur.execute("""
                #     CREATE TABLE IF NOT EXISTS cyclo_product (
                #             link        varchar(255) PRIMARY KEY,
                #             name        varchar(255),
                #             price       varchar(255),
                #             retailer    varchar(255)
                #     )
                # """)
                # self.conn.commit()

            else:
                raise Exception('Tried to retrieve cursor from null database')

            
        except Exception as err:
            print(err)
            self.cur = None

    ###################################################PUBLIC METHODS###################################################


    def start(self, search_term: str):
        print(search_term)
        self.__initDB()
        self.__initCursor()
        self.__initTable()
        data = run_scrapers(search_term)
        self.update_param(data)
        default_retrieve_items(self.conn, self.cur)


    def clear_results(self):
        try:
            if self.conn is None:
                raise Exception('Missing connection')

            if self.cur is None:
                raise Exception('Missing cursor')


            drop_all_tables(self.conn, self.cur)
            create_table(self.conn, self.cur)

            # self.cur.execute("""
            #     CREATE TABLE IF NOT EXISTS cyclo_product (
            #             link        varchar(255) PRIMARY KEY,
            #             name        varchar(255),
            #             price       varchar(255),
            #             retailer    varchar(255)
            #     )
            # """)
            # self.conn.commit()

        except Exception as err:
            print(err)
        return

    def update_param(self, data: list):
        self.clear_results()
        print(data)
        for item in data:
            insert_item(self.conn, self.cur, item)
            #self.cur.execute("""
            #     INSERT INTO cyclo_product(link, name, price, retailer) values(%s, %s, %s, %s)
            #""", (item['url'], item['name'], item['price'], item['retailer'])
            #)

        return

    def get_results(self):
        try:
            if self.conn is None:
                raise Exception('Missing connection')

            if self.cur is None:
                raise Exception('Missing cursor')

            results = []
            for row in self.cur.fetchall():
                results.append(dict(zip([col[0] for col in self.cur.description], row)))
            self.cur.close()
            self.conn.close()
            response = jsonify(results)
            response.headers.add("Access-Control-Allow-Origin", "*")
            print(response)
            # self.clear_results() # wipe for next search
            return response
        except Exception as err:
            print(err)




    def update_page(self):
        return