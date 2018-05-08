from misc import *

def find_max_crossing_subarray(a, low, mid, high):
        left_sum = N_INF
        m = 0
        for i in xrange(mid, low-1, -1):
                m += a[i]
                if m > left_sum:
                        max_left = i
                        left_sum = m
        
        right_sum = N_INF
        m = 0
        for i in xrange(mid + 1, high + 1, 1):
                m += a[i]
                if m > right_sum:
                        max_right = i
                        right_sum = m
        
        return max_left, max_right, left_sum + right_sum

def find_max_subarray(a, low, high):            #分治法
        if low == high:
                return low, high, a[low]
        
        mid = (high + low) / 2
        left_low, left_high, left_sum = find_max_subarray(a, low, mid)
        right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
        else:
                return cross_low, cross_high, cross_sum

def find_max_subarray_brute_force(a):           #暴力求解：运行时间的渐进下界是n的平方
        b = []
        for i in xrange(len(a)):
                for j in xrange(i, len(a)):
                        b.append([i,j,sum(a[i:j+1])])
        return max(b, key = lambda x: x[2])


def find_max_subarray_brute_force_less(a):       #次暴力求解：运行时间的渐进紧确界是n的平方
        b = [None]*len(a)
        for i in xrange(len(a)):
                b[i] = [i, i, N_INF]
                m = 0
                for j in xrange(i, len(a)):
                        m += a[j]
                        if b[i][2] < m:
                                b[i][2] = m
                                b[i][1] = j
        return max(b, key = lambda x: x[2])

def find_max_subarray_linear_time_simple(a):    #线性时间算法
        """
        @wikipedia.org
        Kadane's algorithm begins with a simple inductive question: 
        if we know the maximum subarray sum ending at position i (call this B[i]), what is
        the maximum subarray sum ending at position i+1 (equivalently, what is B[i+1])?
        ……

        Because of the way this algorithm uses optimal substructures (the maximum subarray
        ending at each position is calculated in a simple way from a related but smaller
        and overlapping subproblem: the maximum subarray ending at the previous position) 
        this algorithm can be viewed as a simple/trivial example of dynamic programming.
        """

        b = [None]*len(a)
        b[0] = a[0]
        for i in xrange(1, len(a)):
                b[i] = max(b[i-1]+a[i], a[i])
        return max(b)

def find_max_subarray_linear_time(a):           #线性时间算法（返回起止下标）
        b = [None]*len(a)
        b[0] = [0, 0, a[0]]     #left, right, sum
        for i in xrange(1, len(a)):
                if b[i-1][2] < 0:
                        b[i] = [i, i, a[i]]
                else:
                        b[i] = b[i-1][:]
                        b[i][1] += 1
                        b[i][2] += a[i]
        return max(b, key = lambda x : x[2])

if __name__ == "__main__":
        egs = [
                [1,2,3,-10,-4,100,200,1,2,3,-1,-2,-40,300,-1,-2,-20],
                [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],   #样例（股票价格变化的最大子数组问题）
        ]

        for a in egs:
                low, high, sub_sum = find_max_subarray(a, 0, len(a)-1)
                print "recursive result:\t", sub_sum, a[low:high+1]

                low, high, sub_sum = find_max_subarray_linear_time(a)
                print "linear time result:\t", sub_sum, a[low:high+1]

                low, high, sub_sum = find_max_subarray_brute_force(a)
                print "brute force result:\t", sub_sum, a[low:high+1]

                low, high, sub_sum = find_max_subarray_brute_force_less(a)
                print "less force result:\t", sub_sum, a[low:high+1]
