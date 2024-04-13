import unittest
from bank_account1 import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount("123456", "John Doe", 1000)

    def test_deposit(self):
        self.assertEqual(self.bank_account.deposit(500), "Deposited $500. New balance: $1500")
        self.assertEqual(self.bank_account.deposit(-100), "Invalid amount for deposit.")

    def test_withdraw(self):
        self.assertEqual(self.bank_account.withdraw(500), "Withdrew $500. New balance: $500")
        self.assertEqual(self.bank_account.withdraw(2000), "Insufficient funds or invalid amount for withdrawal.")
        self.assertEqual(self.bank_account.withdraw(-100), "Insufficient funds or invalid amount for withdrawal.")

    def test_display_balance(self):
        self.assertEqual(self.bank_account.display_balance(), "Current Balance: $1000")

if __name__ == "__main__":
    unittest.main()
