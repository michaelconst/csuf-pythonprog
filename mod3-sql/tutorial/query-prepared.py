from contextlib import closing
from datetime import date
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor(prepared=True)
        query = """
        select first_name, last_name
        from actor where first_name like ? and last_name like ?
        """
        # prepare and execute
        c.execute(query, ('A%', 'G%'))
        for row in c.fetchall():
            print('{!s}, {!s}'.format(str(row[0].decode()), str(row[1].decode())))
        # skip preparation and only execute (with the new values)
        c.execute(query, ('C%', 'W%'))
        for row in c.fetchall():
            print('{!s}, {!s}'.format(row[0].decode(), row[1].decode()))
