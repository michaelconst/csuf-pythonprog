from contextlib import closing
from mysql.connector.errors import Error
from mysql.connector.errorcode import *
from utils.helpers import get_config, get_connection


if __name__ == '__main__':
    config = get_config()
    with closing(get_connection(**config)) as conn:
        print('Connection successful')

        c = conn.cursor()
        create_db = """
        CREATE TABLE IF NOT EXISTS %s (
           review_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
           title VARCHAR(50) NOT NULL,
           author_name VARCHAR(30) DEFAULT NULL,
           author_email VARCHAR(40) NOT NULL,
           film_id SMALLINT UNSIGNED NOT NULL,
           review_text TEXT DEFAULT NULL,
           review_date DATETIME NOT NULL,
           PRIMARY KEY  (review_id),
           KEY idx_fk_film_id (film_id),
           CONSTRAINT `fk_review_film` FOREIGN KEY (film_id) REFERENCES film (film_id)
              ON DELETE RESTRICT ON UPDATE CASCADE )ENGINE=InnoDB DEFAULT CHARSET=utf8
        """
        try:
            c.execute(create_db % 'review')
            conn.commit()
        except Error as err:
            if err.errno == ER_TABLE_EXISTS_ERROR:
                print("table already exists")
            else:
                print(err.msg)


