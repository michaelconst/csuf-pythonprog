from contextlib import closing
from mysql.connector import OperationalError
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        create_db = """
        CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8'
        """
        c.execute(create_db % 'test_db')
        conn.commit()

