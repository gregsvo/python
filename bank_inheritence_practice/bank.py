from checking import Checking
from savings import Savings
from customer import Customer
import sys

class Bank:
	
	def __init__(self):
		print("WORKED!")
		self.menu()

	def menu(self):
		print('\n' + '=' * 50)
		print('Welcome to Greg Bank - Your Trusted Partner')
		print('=' * 50 + '\n')
		choice = input('Please enter your choice: \n [L]og In \n [O]pen Account \n [Q]uit \n :').lower()
		
		if choice == 'l':
			self.security_check()
		elif choice == 'o':
			self.open_account()
		elif choice == 'q':
			exit()
		else:
			self.menu()

	def security_check(self):
		print("security check!!")
	
	def deposit(self):
		pass

	def menu_selection(self, choice):
		return 

	def withdraw(self):
		pass

	def get_balance(self):
		pass

	def get_points(self):
		pass

	def open_account(self):
		print("Opening Account!")

	def close_account(self):
		pass

	def get_account_history(self):
		pass

	def earn_interest(self):
		pass

	def exit(self):
		print("EXITING")
		sys.exit()

Bank()