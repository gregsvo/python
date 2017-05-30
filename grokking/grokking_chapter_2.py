import random
from time import time

class Grok(object):
	def __init__(self):
		self.unsorted_list = random.sample(xrange(10000), 10000)
		self.unsorted_list_size = len(self.unsorted_list)
		self.selection_sort_time = 0
		self.selection_sort_step_count = 0
		self.sorted_list = []

	def find_smallest_list_item(self, unsorted_list):
		smallest = unsorted_list[0]
		smallest_index = 0
		for i in range(1, len(unsorted_list)):
			self.selection_sort_step_count += 1
			if unsorted_list[i] < smallest:
				smallest = unsorted_list[i]
				smallest_index = i
		return smallest_index

	def selection_sort(self):
		start_time = time()
		for i in range(1, len(self.unsorted_list)):
			smallest = self.find_smallest_list_item(self.unsorted_list)
			self.sorted_list.append(self.unsorted_list.pop(smallest))
		finish_time = time()
		self.selection_sort_time = finish_time - start_time
		self.times()
		return None

	def times(self):
		print "---------------------"
		print "THE LIST OF {} ITEMS HAS BEEN SUCCESSFULLY SORTED USING: SELECTION_SORT".format(self.unsorted_list_size)
		print "---------------------"
		print "Selection Sort Time: {}     Selection Sort Step Count: {}".format(self.selection_sort_time, self.selection_sort_step_count)
		print "---------------------"

		return None
