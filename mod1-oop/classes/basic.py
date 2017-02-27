class Account:

    print "This is the Account class"

    def __init__(self, name, balance=0.0):
        self.name = name
        assert balance >= 0, "balance must 0 or greater"
        try:
            self.balance = float(balance)
        except TypeError as e:
            print('balance is not a number: %s' % str(e))
            raise

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

    def transfer_to(self, dst_account, amt):
        bal = self.withdraw(amt)
        dst_account.deposit(amt)
        return bal

    @staticmethod
    def transfer(src_account, dst_account, amt):
        src_account.withdraw(amt)
        dst_account.deposit(amt)


if __name__ == "__main__":
    acct = Account("checking")
    # acct2 = Account("savings", -10)

    acct = Account("checking")
    acct.deposit(100)
    # acct.withdraw(200)
    print('account "%s" balance=%d' % (acct.get_name(), acct.get_balance()))

    acct2 = Account("savings", 1000.0)
    acct.transfer_to(acct2, 50)
    Account.transfer(acct2, acct, 200)
    print('account "%s" balance=%d' % (acct.get_name(), acct.get_balance()))
    print('account "%s" balance=%d' % (acct2.get_name(), acct2.get_balance()))