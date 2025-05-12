from transaction import Withdrawal, Deposit, BalanceInquiry

class TransactionFactory:
    @staticmethod
    def create_transaction(transaction_type, account, amount=0):
        if transaction_type == "withdraw":
            return Withdrawal(account, amount)
        elif transaction_type == "deposit":
            return Deposit(account, amount)
        elif transaction_type == "balance":
            return BalanceInquiry(account)
        else:
            raise ValueError("Invalid transaction type")
