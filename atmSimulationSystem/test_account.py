# test_account.py
import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account("123", "1111", 100)

    def test_withdraw(self):
        self.assertTrue(self.acc.withdraw(50))
        self.assertEqual(self.acc.get_balance(), 50)

    def test_withdraw_insufficient(self):
        self.assertFalse(self.acc.withdraw(200))

    def test_deposit(self):
        self.acc.deposit(100)
        self.assertEqual(self.acc.get_balance(), 200)

if __name__ == "__main__":
    unittest.main()
