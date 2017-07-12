import unittest
from Bank_Account import Account

class AccountTestCase(unittest.TestCase):
	def setUp(self):
		self.account_seye = Account()

	def test_balance(self):
		self.assertEqual(self.account_seye.balance, 1000, msg="Account balance wrong")

	def test_deposit(self):
		self.account_seye.deposit(2000)
		self.assertEqual(self.account_seye.balance, 3000)

	def test_withdraw(self):
		self.account_seye.withdraw(500)
		self.assertEqual(self.account_seye.balance, 500)

if __name__ == '__main__':
    unittest.main()		