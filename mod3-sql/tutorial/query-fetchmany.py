from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


def print_all(coll):
    for item in coll:
        print(item)

if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        query = """
        select first_name, last_name
        from actor where first_name like 'A%'
        """
        c.execute(query)
        rows = c.fetchmany()
        print('fetch %d rows' % len(rows))
        print_all(rows)

        rows = c.fetchmany(size=10)
        while rows:
            print('fetched {} out of {} rows'.format(len(rows), 10))
            print_all(rows)
            rows = c.fetchmany(size=10)


