"""
第17章 摊还分析
17.1 聚合分析
"""

k = 8
class Counter(object):
        
        def __init__(self, lst):
                self.A = lst[:]                 #use an array A[0.. k-1]􏰀 of bits
                self.length = len(self.A)       #self.length = k

        def getvalue(self):
                return sum(2**idx for idx, val in enumerate(self.A) if val != 0)

        def increment(self):
                """
                “In general, A[i]􏰀 flips n/2**i times 
                in a sequence of n INCREMENT operations 
                on an initially zero counter.”
                简言之，计数器每自增2**i次，A[i]就要反转1次。
                每自增1次A[0]就要反转
                每自增2次A[1]就要反转
                每自增4次A[2]就要反转
                每自增8次A[3]就要反转

                求和 --> 极限 --> 自增n次，发生反转的总次数<2n

                因此，对一个初值为0的计数器，执行一个n个自增操作的序列的最坏情况时间为O(n)。
                每个操作的平均代价，即摊还代价为O(n)/n=O(1)。
                """

                i = 0
                while i < self.length and self.A[i] == 1:
                        self.A[i] = 0
                        i += 1

                if i < self.length:
                        self.A[i] = 1

if __name__ == "__main__":
        c = Counter([0]*k)  #一个k位二进制计数器，k=8，表达区间[0,255]
        for _ in xrange(2**k):
                c.increment()
                print c.A, c.getvalue()
