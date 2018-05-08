from misc import *

@func_call
def merge(lst, p, q, r):
	L = lst[p:q+1]
	R = lst[q+1:r+1]
	L.append(P_INF)
	R.append(P_INF)
	
	i=j=0
	for k in xrange(p, r+1):
		if L[i] <= R[j]:
			lst[k] = L[i]
			i += 1
		else:
			lst[k] = R[j]
			j += 1

@func_call
def merge_sort(lst, p, r):
	print p,r
	if p < r:
		q = (p + r) / 2
		merge_sort(lst, p, q)
		merge_sort(lst, q+1, r)
		merge(lst, p, q, r)


import random
def main():
	lst = range(6)
	random.shuffle(lst)
	r = lst[:]
	merge_sort(r, 0, len(r)-1)
	print lst,r

	PrintFuncCall()

if __name__ == "__main__":
	main()
