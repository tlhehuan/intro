def minimum(a):
	min = a[0]
	for v in a[1:]:
		if min > v:
			min = v
	return min

def mini_max_mum(a):
	if len(a) == 0:
		return
	
	if len(a)%2 == 0:
		if a[0] > a[1]:
			max = a[0]
			min = a[1]
		else:
			max = a[1]
			min = a[0]
		beg = 2
	else:
		min = max = a[0]
		beg = 1
	
	for i in xrange(beg, len(a), 2):
		if a[i] > a[i + 1]:
			_min = a[i+1]
			_max = a[i]
		else:
			_min = a[i+1]
			_max = a[i]
		
		min = min if _min > min else _min
		max = max if _max < max else _max
	return min, max

if __name__ == "__main__":
	lst = [60,50,40,70,99,100,100,88,87,85,10,20,60]
	print minimum(lst)
	print mini_max_mum(lst)
