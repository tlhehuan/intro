import random

def test(n, m):
	for _ in xrange(n):
		lst = range(m)
		random.shuffle(lst)
		r = insertion_sort(lst)
		print lst ,r

def insertion_sort(lst):
	lst = lst[:]
	for j in xrange(1, len(lst)):
		key = lst[j]
		i = j - 1
		while i >= 0 and lst[i] > key:
			lst[i + 1] = lst[i]
			i -= 1
		lst[i + 1] = key
	return lst

if  __name__ == "__main__":
	test(10, 0)
	test(10, 1)
	test(10, 10)