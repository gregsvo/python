import random
from time import time

class Grok(object):
	def __init__(self):
		self.list = [x for x in range(1,1000000)]
		self.binary_search_time = 0
		self.binary_search_guess_count = 0
		self.simple_search_time = 0
		self.simple_search_guess_count = 0
		self.item = random.randint(1, len(self.list))

	def binary_search(self):
		low = 0
		high = len(self.list) - 1
		self.binary_search_guess_count = 0
		start_time = time()
		while low <= high:
			mid = (low + high ) / 2
			guess = self.list[mid]
			self.binary_search_guess_count += 1
			if guess == self.item:
				found_time = time()
				self.binary_search_time = found_time - start_time
				print "GOT IT! The number was: {}, and it took me {} guesses. Finished search in {}".format(self.item, self.binary_search_guess_count, self.binary_search_time)
				return mid
			elif guess > self.item:
				high = mid - 1
				print "my wrong guess was: {}".format(guess)
			else:
				low = mid + 1
				print "my wrong guess was: {}".format(guess)
		return None

	def simple_search(self):
		start_time = time()
		self.simple_search_guess_count = 0
		guess = 0
		for guess in self.list:
			guess += 1
			self.simple_search_guess_count += 1
			if self.item == guess:
				found_time = time()
				self.simple_search_time = found_time - start_time
				print "GOT IT! The number was: {}, and it took me {} guesses. Finished search in {}".format(self.item, self.simple_search_guess_count, self.simple_search_time)
				break
			else:
				print "my wrong guess was: {}".format(guess)

	def times(self):
		print "---------------------"
		print "Binary Search Time: {}      Binary Search Guess Count: {}".format(self.binary_search_time, self.binary_search_guess_count)
		print "---------------------"
		print "Simple Search Time: {}      Binary Search Guess Count: {}".format(self.simple_search_time, self.simple_search_guess_count)
		print "---------------------"


		return None