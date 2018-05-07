
import random

def left(i):
	return 2 * i + 1

def right(i):
	return 2 * i + 2

def parent(i):
	return (i - 1) / 2

class heap(object):
	def __init__(self, lst):
		self.lst = lst[:]
		self.size = len(lst)
	
	def heapsort(self):
		self.build_maxheap()
		print self.lst
		for i in xrange(len(self.lst) - 1, 0, -1):
			self.lst[i], self.lst[0] = self.lst[0], self.lst[i]
			self.size -= 1	#影响递归
			self.max_heapify(0)
	
	def max_heapify(self, i):
		l = left(i)
		r = right(i)
		print "size=%2d, i=%2d, left=%2d, right=%2d"%(self.size, i, l, r)
		if l < self.size and self.lst[i] < self.lst[l]:
			largest = l
		else:
			largest = i
		
		if r < self.size and self.lst[largest] < self.lst[r]:
			largest = r
		if i != largest:
			self.lst[i], self.lst[largest] = self.lst[largest], self.lst[i]
			self.max_heapify(largest)
	
	def build_maxheap(self):
		self.size = len(self.lst)
		for i in xrange(self.size/2 - 1, -1, -1):
			self.max_heapify(i)

		
if __name__ == "__main__":
	lst = range(10)
	random.shuffle(lst)
	print lst
	hp = heap(lst)
	hp.heapsort()
	print hp.lst
