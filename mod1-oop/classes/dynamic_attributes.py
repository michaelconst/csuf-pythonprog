class Account:
    def __init__(self, name, acctno, balance=0):
        self.name = name
        self.__acctno = acctno
        assert balance >= 0, "balance must 0 or greater"
        try:
            self.__balance = float(balance)
        except TypeError as e:
            print('balance is not a number: %s' % str(e))
            raise
        self.linked_accounts = list()

    def withdraw(self, amt):
        if amt > self.balance:
            raise ValueError("account cannot be overdrawn")
        self.balance -= amt
        return self.balance

    def deposit(self, amt):
        self.balance += amt
        return self.balance

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    @property
    def balance(self):
        return self.__balance

    @property
    def acctno(self):
        return self.__acctno

    def transfer_to(self, dst_account, amt):
        bal = self.withdraw(amt)
        dst_account.deposit(amt)
        return bal

    def link_account(self, account):
        if self.get_linked_account_by_acctno(account.acctno) is None:
            # account is not already linked
            self.linked_accounts.append(account)

    def get_linked_account_by_acctno(self, acctno):
        matches = filter(lambda a: a.__acctno == acctno, self.linked_accounts)
        if len(matches) > 0:
            return matches[0]

    def get_linked_account_by_name(self, name):
        matches = filter(lambda a: a.name == name, self.linked_accounts)
        if len(matches) > 0:
            return matches[0]

    @staticmethod
    def transfer(src_account, dst_account, amt):
        src_account.withdraw(amt)
        dst_account.deposit(amt)

    def __getattr__(self, name):
        names = [a.name for a in self.linked_accounts]
        if name in names:
            return self.get_linked_account_by_name(name)
        msg = '{.__name__!r} has no attribute {!r}'
        raise AttributeError(msg.format(self.__class__, name))


if __name__ == "__main__":
    acct1 = Account("checking", "101234", 100)
    acct2 = Account("savings", "101235", 1000)
    acct3 = Account("BofA", "10702", 500)

    acct1.link_account(acct2)
    acct1.link_account(acct3)

    # get balance of a linked account
    msg = '{!r} balance is {:4.2f}'
    print(msg.format("BofA", acct1.get_linked_account_by_name("BofA").balance))
    print(msg.format("BofA", acct1.BofA.balance))
