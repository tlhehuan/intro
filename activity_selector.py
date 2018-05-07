#算法导论 第16章 活动选择问题

def recursive_activity_selector(s,f,i,j):       #贪心算法递归
        m = i + 1
        while m < j and s[m] < f[i]:
                m += 1
        
        if m < j:
                return [m] + recursive_activity_selector(s, f, m, j)
        else:
                return []

def iterative_activity_selector(s, f, i, j):          #贪心算法迭代
        k = i + 1
        r = [k]
        for m in xrange(i+2, j):
                if s[m] >= f[k]:
                        r += [m]
                        k = m
        return r

def natrual_recursive(s, f, i, j):
        if i == j:
                return 1
        
        lc = {}
        rc = {}
        for k in xrange(i+1, j):        #不含i,j
                left(s,f,i,j,k,lc)
                right(s,f,i,j,k,rc)
        
        for k in xrange(i+1, j):
                print "k =",k, "max =", lc[k]+rc[k]+1
        return max(lc[k]+rc[k]+1 for k in xrange(i+1, j))

def left(s, f, i, j, k, r):
        q = r.get(k)
        if q != None:
                return q
        
        lst = [m for m in xrange(i+1, j) if s[k] >= f[m]]
        if len(lst) == 0:
                q = 0
        else:
                q = max(left(s,f,i,j,m,r) + 1 for m in lst)
        r[k] = q
        return q

def right(s, f, i, j, k, r):
        q = r.get(k)
        if q != None:
                return q

        lst = [m for m in xrange(i+1, j) if f[k] <= s[m]]
        if len(lst) == 0:
                q = 0
        else:
                q = max(right(s,f,i,j,m,r) + 1 for m in lst)
        r[k] = q
        return q

def bottom_up(s,f,i,j):
        ld = {}
        for k in xrange(i+1, j):        #不含i,j
                ld[k] = []
                
                for m in xrange(i+1, k):        #找k的左兼容活动，不含k
                        #如果活动序列没有排序，则把区间改为(i+1,j)，并在此跳过k自身
                        if s[k] >= f[m]:
                                ld[k].append(m)
        lc = {}
        for k in xrange(i+1, j):
                lc[k] = 0 if len(ld[k]) == 0 else 1+max(lc[m] for m in ld[k])
        print lc

        rd ={}
        for k in xrange(i+1, j):        #不含i,j
                rd[k] = []

                for m in xrange(i+1, j):        #找k的右兼容活动，不含k
                        #跳过k自身
                        if m==k:
                                continue
                        if f[k] <= s[m]:
                                rd[k].append(m)
        rc = {}
        for k in xrange(j-1, i, -1):    #不含i,j
                rc[k] = 0 if len(rd[k]) == 0 else 1+max(rc[m] for m in rd[k])
        print rc

        for k in xrange(i+1, j):
                print "k =",k, "max =", lc[k]+rc[k]+1
        return max(lc[k]+rc[k]+1 for k in xrange(i+1, j))

if __name__ == "__main__":
        #问题：选出一个最大兼容活动集
        s=[0,1,3,0,5,3,5,6,8,8,2,12]      #开始时间
        f=[0,4,5,6,7,9,9,10,11,12,14,16]  #结束时间(已按结束时间排序)
        
        print "动态规划"
        print natrual_recursive(s, f, 0, 12)
        print bottom_up(s, f, 0, 12)
        
        print "贪心算法"
        print recursive_activity_selector(s, f, 0, 12)
        print iterative_activity_selector(s, f, 0, 12)
