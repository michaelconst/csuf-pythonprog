from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        query = """
        select *
        from actor where first_name like 'A%'
        """
        c.execute(query)
        print(', '.join(c.column_names))
        print('number of rows=%d' % c.rowcount)
        c.fetchall()
        print('number of rows=%d' % c.rowcount)
        c1 = conn.cursor(buffered=True)
        c1.execute(query)
        print('number of rows=%d' % c.rowcount)


        query2 = """
        select first_name, last_name
        from actor where first_name like 'A%'
        """
        c2 = conn.cursor(dictionary=True)
        c2.execute(query)
        for row in c2:
            print('{first_name}, {last_name}'.format(**row))

        c3 = conn.cursor(named_tuple=True)
        c3.execute(query)
        for row in c3:
            print('{first_name}, {last_name}'.format(first_name=row.first_name, last_name=row.last_name))
