from account import Account

class Savings(Account):
	interest_rate = 1.7
	account_type = 'savings'
	can_overdraw = False