# 《算法导论》第15章 动态规划
# “Whenever a recursion tree for the natural recursive solution to a problem
# contains the same subproblem repeatedly, and the total number of distinct
# subproblems is small, dynamic programming can improve efficiency,
# sometimes dramatically.”

# 一般思路：刻画一个最优解的结构特征、递归定义最优解的值、自底向上计算
# 适用动态规划的两个要素：最优子结构和子问题重叠

# e.g. 腾讯光子面试题：一个M*N的棋盘格，求左下角走到右上角有多少种走法

from misc import *

#自顶向下递归
@func_call
def walk(m, n):
        if m == 1 or n == 1:
                return 1
        else:
                return walk(m-1, n) + walk(m, n-1)

#自底向上
@func_call
def bottom_up_walk(m, n):
        r = [1]*m*n     #从左下角开始逐行依次填表
        for i in xrange(1, m):
                for j in xrange(1, n):
                        r[i*n+j] = r[(i-1)*n+j] + r[i*n+j-1]
        return r[m*n-1]

if __name__ == "__main__":
        print walk(6, 4)
        print bottom_up_walk(6, 4)
        PrintFuncCall()

