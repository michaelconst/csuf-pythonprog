from contextlib import closing
from datetime import datetime
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        func = "SELECT get_customer_balance(%s, %s) as x"
        customer_id = 577
        dt = datetime(2015, 6, 30, 18, 5, 30)
        result = c.execute(func, (customer_id, dt))
        val = c.fetchone()
        print('balance={}'.format(val[0]))


