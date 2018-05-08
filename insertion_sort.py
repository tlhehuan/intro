import random

def insertion_sort(lst):
	for j in xrange(1, len(lst)):	#循环n-1次
		key = lst[j]
		i = j - 1
		while i >= 0 and lst[i] > key:
			lst[i + 1] = lst[i]
			i -= 1
		lst[i + 1] = key
	return lst

if  __name__ == "__main__":
	lst = range(20)
	random.shuffle(lst)

	print lst
	insertion_sort(lst)
	print lst
