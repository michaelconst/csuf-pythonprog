from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        query = """
        select rental_date, return_date, datediff(return_date, rental_date) as duration
        from rental where rental_date >= %s and rental_date <= %s
        having duration > %s
        order by rental_date
        """
        from_ = date(2005, 6, 1)
        to_ = date(2005, 6, 30)
        c.execute(query, (from_, to_, 9))
        for rental_date, return_date, duration in c:
            print('rented at {}, returned at {} ({} days)'.format(rental_date, return_date, duration))

