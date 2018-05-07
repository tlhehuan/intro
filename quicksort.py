import random

def partition(lst, p, r):
	x = lst[r]
	i = p - 1
	for j in xrange(p, r):
		if lst[j] <= x:
			i = i + 1
			lst[i], lst[j] = lst[j], lst[i]
	
	lst[i+1], lst[r] = lst[r], lst[i+1]
	return i + 1

def quicksort(lst,p,r):
	if p < r:
		q = partition(lst, p, r)
		print q
		print p, q-1, q + 1, r
		quicksort(lst, p, q-1)
		quicksort(lst, q + 1, r)

if __name__ == "__main__":
	#lst = range(10)
	#random.shuffle(lst)
	lst = [6, 0, 5, 1, 2, 4, 3, 8, 7, 9]
	rlst = lst[:]
	quicksort(lst, 0, len(lst) -1)
	print rlst, lst
