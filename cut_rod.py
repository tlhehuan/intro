
from misc import *

#自顶向下递归实现
def cut_rod(p, n):
        if n == 0:
                return 0

        #将钢条从左边切割下长度为i的一段不再切割，只对右边剩下的长度为n-i的一段继续切割（递归求解）
        #依据公式15.2（特别注意跟15.1的公式对比）
        #注意回顾图15-3 递归调用树
        q = N_INF
        for i in xrange(1, n+1):
                q = max(q, p[i] + cut_rod(p, n-i))
        return q

#带备忘的自顶向下递归实现
def memoized_cut_rod(p, n):
        r = [N_INF]*(n+1)
        return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
        if r[n] != N_INF:
                return r[n]
        if n == 0:
                q = 0
        else:
                q = N_INF
                for i in xrange(1, n+1):
                        q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
        r[n] = q
        return q

#自底向上法
def bottom_up_cut_rod(p, n):
        r = [N_INF]*(n+1)        #依次求解规模为j=0,1,……,n的子问题
        r[0] = 0
        for j in xrange(1, n+1):
                q = N_INF
                for i in xrange(1, j+1):
                        q = max(q, p[i] + r[j-i])
                r[j] = q
        return r[n]

if __name__ == "__main__":
        #给定一段长度为n的钢条和一个价格表，求切割方案，使得销售收益最大
        #如果长度为n的钢条价格p(n)足够大，最优解可能就是完全不需要切割
        p = [0,1,5,8,9,10,17,17,20,24,30]       #价格表（0长钢条价格为0）
        for n in xrange(1, 11):
                print cut_rod(p, n)
                print memoized_cut_rod(p, n)
                print bottom_up_cut_rod(p, n)