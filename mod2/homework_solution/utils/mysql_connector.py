import mysql.connector
from mysql.connector import errorcode
from configparser import ConfigParser


# Database connection Class
class DbConnector(object):
    """
        Python Class for connecting  with MySQL server.
    """

    # __init__ function
    def __init__(self, filename='mysqldb_config.ini', section='mysql'):
        try:
            parser = ConfigParser()
            parser.read(filename)
            # get section, default to mysql
            db = {}
            if parser.has_section(section):
                items = parser.items(section)
                for item in items:
                    db[item[0]] = item[1]
            else:
                raise Exception('{0} not found in the {1} file'.format(section, filename))

            self.__host = db.get('host', '127.0.0.1')
            self.__user = db.get('user', 'root')
            self.__password = db.get('password', '')
            self.__database = db.get('database', 'test')
            self.__connection = None
            self.__cursor = None
            self.sqlout = None

            # connect in init
            self.connect()
        except FileNotFoundError as errNotFound:
            print(errNotFound)
        except IOError as ioErr:
            print(ioErr)

    def connect(self):
        try:
            self.__connection = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database)
            self.__cursor = self.__connection.cursor(buffered=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database {} does not exist".format(self.__database))
            else:
                print(err)
                raise
        else:
            print("Connection successful.")

    def execute(self, sql):
        return self.__cursor.execute(sql)

    def execute_with_params(self, sql, params):
        return self.__cursor.execute(sql, params)

    def query(self, sql):
        try:
            self.__cursor.execute(sql)
            self.sqlout = self.__cursor.fetchall()
            return self.sqlout
        except mysql.connector.Error as e:
            print(e)

    def query_with_params(self, sql, params):
        try:
            self.__cursor.execute(sql, (params))
            self.sqlout = self.__cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)

    def rows(self):
        return self.__cursor.rowcount

    def tables_and_columns(self):
        qtables = "SHOW TABLES FROM {}".format(self.__database)
        self.query(qtables)
        print("Number of tables in '{}' database: {} ".format(self.__database, self.rows()))
        print(self.sqlout)
        print('\n')
        for (table_name,) in self.sqlout:
            q = "SHOW COLUMNS FROM {}".format(table_name)
            self.query(q)
            print("Result of the Query: " + q)
            print("Number of Columns in table '{}': ".format(table_name) + str(db.rows()))
            for item in db.sqlout:
                print(item)

            print('\n')

    def query_fetch_one(self, sqlquery):
        try:
            self.__cursor.execute(sqlquery)
            self.sqlout = self.__cursor.fetchone()
            while self.sqlout is not None:
                print(self.sqlout)
                self.sqlout = self.__cursor.fetchone()
        except mysql.connector.Error as e:
            print(e)

    def query_fetch_all(self, sqlquery):
        try:
            self.__cursor.execute(sqlquery)
            self.sqlout = self.__cursor.fetchall()
            rowcount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowcount))
            for row in self.sqlout:
                print(row)
        except mysql.connector.Error as e:
            print(e)

    # end-fetchall

    # fetchmany Query
    def query_fetch_many(self, sqlquery, size=10):

        def batch(cursor, size):
            while True:
                rows = cursor.fetchmany(size)
                if not rows:
                    break
                for row in rows:
                    yield row
        try:
            self.__cursor.execute(sqlquery)
            self.sqlout = self.__cursor.fetchmany(size)
            rowcount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowcount))

            for row in batch(self.__cursor,size):
                print(row)
        except mysql.connector.Error as e:
            print(e)

    def query_fetch_many1(self, sqlquery, size=10):

        def batch(cursor, size):
            while True:
                rows = cursor.fetchmany(size)
                if not rows:
                    break
                for row in rows:
                    yield row

        try:
            self.__cursor.execute(sqlquery)
            self.sqlout = self.__cursor.fetchmany(size)
            rowcount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowcount))

            rows1 = batch(self.__cursor, size)
            for row in rows1:
                print(row)
        except mysql.connector.Error as e:
            print(e)

    def print_query_results(self, query):
        self.query(query)
        print("Number of Rows: " + str(self.rows()))
        # Print data
        print("Result of the Query: " + query)
        for item in self.sqlout:
            print(item)

    def close(self):
        # Close DB connection
        if self.__connection:
            self.__connection.close()
        print('Database connection closed')

    def __del__(self):
        self.close()


# instantiate DbConnector class object
db = DbConnector('mysqldb_config.ini', 'mysql')



