from configparser import ConfigParser
import mysql.connector
from mysql.connector import errorcode, OperationalError


def get_config(fn='utils/mysqldb_config.ini', section='mysql'):
    try:
        parser = ConfigParser()
        parser.read(fn)
        # get section, default to mysql
        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
            return db
        else:
            raise Exception('{0} not found in the {1} file'.format(section, fn))
    except (FileNotFoundError, IOError) as err:
        print(err)


def get_connection(**kwargs):
    try:
        return mysql.connector.connect(**kwargs)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Invalid user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        raise OperationalError(err)