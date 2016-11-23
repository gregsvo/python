import datetime
import webbrowser

class WikiDate(object):
	def __init__(self):
		self.get_wiki_date()

	def get_wiki_date(self):
		
		while True:
			user_date = input("Month and day you want wiki for (MM DD): ")
			try:
				print("Finding wiki for {}...".format(user_date))
				user_date_parsed = datetime.datetime.strptime('{}'.format(user_date), '%m %d')
				user_date_string = user_date_parsed.strftime('%B_%d')
				url = "https://en.wikipedia.org/wiki/{}".format(user_date_string)
				webbrowser.open(url,new=2)
				break
			except ValueError:
				print("That is not a valid date. Try again.")

WikiDate()