def counting_sort(a,k):
	b = [None]*len(a)
	
	c = [0] * k
	for v in a:
		c[v] += 1
	print c
	
	for i in xrange(1, k):
		c[i] += c[i - 1]
	print c
	
	for va in a[::-1]:
		b[c[va]-1]=va
		c[va] -= 1
	
	print a, b

if __name__ == "__main__":
	lst = [9,8,4,6,7,7,9,1,3,2,0]
	counting_sort(lst, 10)
