from account import Account


class Checking(Account):
	interest_rate = 0.7
	account_type = 'checking'
	can_overdraw = True
	