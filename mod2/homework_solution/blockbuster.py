from homework_solution.utils.mysql_connector import DbConnector


class BBAccount:
    def __init__(self, customer_id, connector=None):
        self.__customer_id = customer_id
        self.__connector = connector
        if self.__connector is None:
            self.__connector = DbConnector()

    def _get_staffer(self, inventory_id):
        sql = "SELECT s.staff_id FROM staff AS s INNER JOIN ON inventory AS i WHERE s.store_id = i.store_id " \
              "AND i.inventory_id = %s"
        self.__connector.query_with_params(sql, (inventory_id,))
        num_staff = len(self.__connector.sqlout)
        if num_staff == 1:
            return self.__connector.sqlout[0]
        else:
            import random
            return self.__connector.sqlout[random.randint(0, num_staff-1)]

    def rent_dvd(self, inventory_id, rental_date):
        # TODO us
        # check if inventory item is in stock
        sql_func = "CALL INVENTORY_IN_STOCK(%s)"
        if self.__connector.execute_with_params(sql_func, (inventory_id,)):
            staff_id = self._get_staffer(inventory_id)
            # insert a row in the rental table
            sql_insert_rental = "INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id) VALUES(%s, %s, %s, %s)"
            self.__connector.execute_with_params(
                sql_insert_rental, (rental_date, inventory_id, self.__customer_id, staff_id))
            # get my current balance
            sql_get_bal = "CALL get_customer_balance(%s, %s)"
            balance = self.__connector.execute_with_params(sql_get_bal, self.__customer_id)
            # insert into the payment table
            sql_insert_pmt = "INSERT INTO payment (customer_id, staff_id, rental_id, amount,  payment_date) " \
                             "VALUES(%s, %s, LAST_INSERT_ID(), %s, %s)"
            self.__connector.execute_with_params(sql_insert_pmt, (self.__customer_id, staff_id, balance, rental_date))

    def return_dvd(self, inventory_id, return_date):
        # TODO us
        pass

    def find_movie_in_stock(self, text_in_title):
        """
        Finds all stores which have this movie in stock.
        :param text_in_title: the movie contains this text as is (i.e. as if quoted) somewhere in its title
        :return: a list of inventory items [inventory_id,...]
        """

    def _get_store_address(self, inventory_id):
        """
        Find the store address
        :param inventory_id:
        :return: the addess of the store which has this inventory item
        """

    def _print_stores(self, inventory_items):
        def compose(f, g):
            return lambda x: f(g(x))

        print('\n'.join([self._get_store_address(item) for item in inventory_items]))

    def find_movie_rented_out(self, text_in_title):
        """
        Find all stores which have the movie rented out.
        :param text_in_title: the movie contains this text as is (i.e. as if quoted) somewhere in its title
        :return: a list of tuples like [(inventory_id, due_date),...]
        """

    def amount_spent_in_month(self, month_number):
        """
        Find how much money I spent on movies in month <month_number>
        :param month_number: 1 for Jan, 2 for Feb, etc. from 1st day of the month to its last, inclusive
        :return: total amount spent on rentals (rental fees, late fees, etc.)
        """