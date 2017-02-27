from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


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
        row = c.fetchone()
        while row is not None:
            print(row)
            row = c.fetchone()

