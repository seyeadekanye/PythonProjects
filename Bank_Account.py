class Account:
	def __init__(self, balance = 1000):
		self.balance = balance

	def check_balance(self):
		return self.balance

	def deposit(self,amount):
		self.balance += amount

	def withdraw(self,amount):
		if self.balance < amount:
			print ('Insufficient Funds!')
		else:
			self.balance -= amount

