from contextlib import closing
from mysql.connector import OperationalError
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        delete_pmt = """
        delete from payment where customer_id = %s and DATE(payment_date) = %s
        """
        delete_rental = """
        delete from rental where customer_id = %s and DATE(rental_date) = %s
        """
        customer_id = 96
        date = '2017-02-06'
        try:
            c.execute(delete_pmt, (customer_id, date))
            print('delete from payment: {}'.format(c.statement))
            print('delete {} rows from payment'.format(c.rowcount))
            c.execute(delete_rental, (customer_id, date))
            print('delete from rental: {}'.format(c.statement))
            print('delete {} rows from rental'.format(c.rowcount))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()


