class BankAccount:
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):

        if value < 0:
            raise ValueError("Balance should not be negetive")

        self._balance = value


acc = BankAccount()
acc.balance = 100
acc.balance = -100
