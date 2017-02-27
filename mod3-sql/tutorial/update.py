from contextlib import closing
from mysql.connector import OperationalError
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        update = """
        update customer as c, address as a
        set c.email = %s, a.phone = %s
        where c.address_id = a.address_id and c.customer_id = 100;
        """
        email = 'robin.hayes@yahoo.com'
        phone = '949-555-1234'
        c.execute(update, (email, phone))
        conn.commit()

