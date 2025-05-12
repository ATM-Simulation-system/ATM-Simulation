from account import Account
from transaction_factory import TransactionFactory

class ATM:
    _instance = None

    def __init__(self):
        self.accounts = {
            "123456": Account("123456", "1234", 1000),
            "654321": Account("654321", "4321", 500),
            "222011": Account("222011", "1111", 5000),
            "333022": Account("333022", "2222", 1500),
            "222012": Account("222012", "3333", 5000)
        }
        self.current_account = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = ATM()
        return cls._instance

    def authenticate(self, acc_number, pin):
        account = self.accounts.get(acc_number)
        if account and account.check_pin(pin):
            self.current_account = account
            return True
        return False

    def perform_transaction(self, txn_type, amount=0):
        transaction = TransactionFactory.create_transaction(txn_type, self.current_account, amount)
        return transaction.execute()
