import MySQLdb as mysql
from MySQLdb.constants import ER
import sys
from configparser import ConfigParser

DB_NAME = "employees"


# Database connection Class
class MySqlDbPythonConnector(object):
    """
        Python Class for connecting  with MySQL server.
    """

    # member variables - private
    __host = None
    __user = None
    __password = None
    __database = None
    __connection = None
    __cursor = None
    #to store the result of the sql query
    sqlout = None

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


            self.__host = db.get('host','127.0.0.1')
            self.__user = db.get('user','root')
            self.__password = db.get('password','')
            self.__database = db.get('database','test')
            #connect in init
            self.connect()
        except FileNotFoundError as errNotFound:
            print(errNotFound)
        except IOError as ioErr:
            print(ioErr)

    # End def __init__

    # connect
    def connect(self):
        try:
            self.__connection = mysql.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database)
            self.__cursor = self.__connection.cursor(buffered=True)
        except mysql.Error as err:
            if err.args[0] == ER.ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.args[0] == ER.BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                sys.exit(1)
        else:
            print("Connection successful.")
    ## End def __connect

    #query
    def query(self, sql):
        try:
            self.__cursor.execute(sql)
            self.sqlout = self.__cursor.fetchall()
            return self.sqlout
        except mysql.Error as e:
            print(e)
    # end-query

    #query With Params
    def queryP(self, sql, params):
        try:
            self.__cursor.execute(sql,(params))
            self.sqlout = self.__cursor.fetchall()
        except mysql.Error as e:
            print(e)
    # end-queryP

    #row count
    def rows(self):
        return self.__cursor.rowcount
    ## end-rowcount

    #print all tables and each table columns
    def tablesAndColumns(self):
        qtables = "SHOW TABLES FROM {}".format(DB_NAME)
        self.query(qtables)
        print("Number of tables in '{}' database: {} ".format(DB_NAME,self.rows()))
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

    #end tablesAnd Columns

    #fetchone Query
    def QueryfetchOne(self, sqlQuery):
        try:
            self.__cursor.execute(sqlQuery)
            self.sqlout = self.__cursor.fetchone()
            while self.sqlout is not None:
                print(self.sqlout)
                self.sqlout = self.__cursor.fetchone()
        except mysql.Error as e:
            print(e)

    #end of fetchone

    # fetchall Query
    def QueryfetchAll(self, sqlQuery):
        try:
            self.__cursor.execute(sqlQuery)
            self.sqlout = self.__cursor.fetchall()
            rowCount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowCount))
            for row in self.sqlout:
                print(row)
        except mysql.Error as e:
            print(e)

    # end-fetchall

    # fetchmany Query
    def QueryfetchMany(self, sqlQuery, size=10):
        #helper function to batch the query
        batchCount = 0
        def batch(cursor, size):
            #print("Batch: " + str(++batchCount))
            while True:
                rows = cursor.fetchmany(size)
                if not rows:
                    break
                for row in rows:
                    yield row
        try:
            self.__cursor.execute(sqlQuery)
            self.sqlout = self.__cursor.fetchmany(size)
            rowCount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowCount))

            for row in batch(self.__cursor,size):
                print(row)
        except mysql.Error as e:
            print(e)
    # end-fetchmany

    # fetchmany Query
    def QueryfetchMany1(self, sqlQuery, size=10):
        # helper function to batch the query
        batchCount = 0
        def batch(cursor, size):
            # print("Batch: " + str(++batchCount))
            while True:
                rows = cursor.fetchmany(size)
                if not rows:
                    break
                for row in rows:
                    yield row
                    #print("Batch: " + str(++batchCount))

        try:
            self.__cursor.execute(sqlQuery)
            self.sqlout = self.__cursor.fetchmany(size)
            rowCount = self.__cursor.rowcount
            print("Number of rows: {}".format(rowCount))

            rows1 = batch(self.__cursor, size)
            for row in rows1:
                print(row)


        except mysql.Error as e:
            print(e)
    # end-fetchmany


    #printQuery
    def printQueryResults(self,query):
        self.query(query)
        print("Number of Rows: " + str(self.rows()))
        # Print data
        print("Result of the Query: " + query)
        for item in self.sqlout:
            print(item)

    # close
    def close(self):
        # Close DB connection
        if self.__connection:
            self.__connection.close()
        print('Database connection closed')
    # End def __close

    # destructor
    def __del__(self):
        self.close()
    # end - destructor

# end PythonMySQLConnector class

# instantiate MySqlDbPythonConnector class object
db = MySqlDbPythonConnector('mysqldb_config.ini','mysql')
table = 'salaries'
tables = ['current_dept_emp','departments', 'dept_emp', 'dept_emp_latest_date','dept_manager', 'employees','salaries','titles']
sqlQ1 = "SHOW TABLES FROM {}".format(DB_NAME)
sqlQ2 = "SHOW COLUMNS FROM {}".format(table)
sqlQ21 = "SHOW COLUMNS FROM %s"
sqlQ211 = '''SHOW COLUMNS FROM %s '''
sqlQ3 = "SELECT emp_no, first_name, last_name, gender FROM employees LIMIT 100"
sqlQ4 = "SELECT emp_no, first_name, last_name, gender FROM employees ORDER BY last_name ASC LIMIT 100"
sqlQ5 = "SELECT COUNT(emp_no) FROM employees"
sqlQ6 = "SELECT last_name, COUNT(emp_no) AS num_emp FROM employees GROUP BY last_name ORDER BY num_emp DESC"
sqlQ7 = "SHOW TABLES FROM employees"
sqlQ8 = 'SELECT * FROM  {} LIMIT 100'.format(table)

sqlQ9 = 'SELECT * FROM  {}'.format(table)



#sqlQ10 = "SELECT employees.last_name, employees.first_name, salaries.salary FROM employees INNER JOIN salaries on employees.emp_no = salaries.emp_no LIMIT 100"
sqlQ10 = "SELECT employees.emp_no, salaries.salary FROM employees LEFT JOIN salaries on employees.emp_no = salaries.emp_no LIMIT 100"
sqlQ11 = 'SELECT * FROM  employees LIMIT 100'
sqlQ = sqlQ9
#db.QueryfetchAll(sqlQ)
#db.QueryfetchMany1(sqlQ8,10)
db.printQueryResults(sqlQ)

#db.tablesAndColumns()
del db


