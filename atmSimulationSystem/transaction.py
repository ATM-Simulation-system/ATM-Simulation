from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, account):
        self.account = account

    @abstractmethod
    def execute(self):
        pass

class Withdrawal(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.amount = amount

    def execute(self):
        return self.account.withdraw(self.amount)

class Deposit(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)
        return True

class BalanceInquiry(Transaction):
    def execute(self):
        return self.account.get_balance()
