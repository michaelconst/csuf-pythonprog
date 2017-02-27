from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        inputs = c.callproc('film_in_stock', (4, 1, 0))
        print('items in stock=%d' % inputs[2])
        # inputs = c.callproc('film_in_stock', (4, 1, (0, 'CHAR(4)')))
        # print('items in stock=%s' % inputs[2])
        result_sets = c.stored_results()
        for rs in result_sets:
            items = [str(i[0]) for i in rs]
            print(', '.join(items))
