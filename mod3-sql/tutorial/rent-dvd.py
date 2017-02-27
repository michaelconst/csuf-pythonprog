from contextlib import closing
from mysql.connector import OperationalError
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        insert_rental = """
        INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
            VALUES(NOW(), %s, %s, %s);
        """
        insert_pmt = """
        INSERT INTO payment (customer_id, staff_id, rental_id, amount,  payment_date)
            VALUES(%(customer_id)s, %(staff_id)s, LAST_INSERT_ID(), %(amount)s, NOW());
        """
        inventory_id = 38
        customer_id = 96
        staff_id = 1
        amount = 2.99
        payment_data = {
            'customer_id': customer_id,
            'staff_id': staff_id,
            'amount': amount
        }
        try:
            c.execute(insert_rental, (inventory_id, customer_id, staff_id))
            print('inserted {} row in table rental'.format(c.rowcount))
            c.execute(insert_pmt, payment_data)
            print('inserted {} row in table payment'.format(c.rowcount))
            conn.commit()
        except OperationalError as e:
            print('failed to rent DVD (inventory id={}) to customer (customer_id={}, error={}'
                  .format(inventory_id, customer_id, str(e)))
            conn.rollback()

        inventory_id = 817
        customer_id = 99
        staff_id = 2
        amount = 4.99
        payment_data = {
            'customer_id': customer_id,
            'staff_id': 5,
            'amount': amount
        }
        try:
            c.execute(insert_rental, (inventory_id, customer_id, staff_id))
            print('inserted {} row in table rental'.format(c.rowcount))
            c.execute(insert_pmt, payment_data)
            print('inserted {} row in table payment'.format(c.rowcount))
            conn.commit()
        except Exception as e:
            print('failed to rent DVD (inventory id={}) to customer (customer_id={}, error={}'
                  .format(inventory_id, customer_id, str(e)))
            conn.rollback()


