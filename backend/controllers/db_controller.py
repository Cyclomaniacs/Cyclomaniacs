import psycopg2
from flask import jsonify

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
                password='admin',
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

    ###################################################PUBLIC METHODS###################################################
    def update_param(self):
        return


    def start(self, search_term: str):
        #run_scrapers(search_term)
        print(search_term)
        self.__initDB()
        self.__initCursor()
        self.cur.execute("""
            SELECT * FROM sells
        """)
        self.conn.commit()


    def get_results(self):
        try:
            if self.conn is None:
                raise Exception('Missing connection')

            if self.cur is None:
                raise Exception('Missing cursor')

            results = self.cur.fetchall()
            data = []
            columns = [col[0] for col in self.cur.description]
            for row in results:
                data.append(dict(zip(columns, row)))
            self.cur.close()
            self.conn.close()
            return jsonify(data)
        except Exception as err:
            print(err)


    def clear_results(self):
        return


    def update_page(self):
        return