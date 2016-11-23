class Customer:
	name = None

	def __init__(self, **kwargs):
		self.points = 0
		self.name = self.create_customer_name()
		self.ssn = self.create_customer_ssn()	

		for key, value in kwargs.items():
			setattr(self, key, value)
	

	def create_customer_name(self):
		return input("Customer Name: ")

	def create_customer_ssn(self):
		while True:
			try:
				self.ssn = int(input("SSN: "))
			except ValueError:
				print("Not a valid SSN. Please type w/ no dashes.")
				continue
			else:
				break
		return self.ssn




		
		




