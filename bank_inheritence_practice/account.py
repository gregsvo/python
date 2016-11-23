import random


class Account(object):
	balance = None
	interest_rate = None
	customer_name = None
	account_type = None

	def __init__(self, **kwargs):
		self.account_number = self.create_account_number()
		for key, value in kwargs.items():
			setattr(self, key, value)
		if self.balance == None:
			self.balance = self.create_starting_balance()
		if self.customer_name == None:
			self.customer_name = self.create_customer_name()


	def __str__(self):
		return "{}'s' {} account has a ${} balance, gaining %{} interest.".format(self.customer_name, self.__class__.__name__, self.balance, self.interest_rate)
		
	def get_balance(self):
		return self.balance

	def get_account_number(self):
		return self.account_number

	def create_account_number(self):
		return random.randint(100000,999999)

	def create_starting_balance(self):
		while True:
			try:
				starting_balance = float(input("Starting Balance: $"))
			except ValueError:
				print("Not a valid starting balance.")
				continue
			else:
				break
		return starting_balance

	def create_customer_name(self):
		return input("Customer Name: ")

	def is_overdrawn(self):
		if self.balance < 0:
			return True
		else:
			return False
	