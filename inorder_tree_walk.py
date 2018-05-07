def left(i):
	return 2 * i + 1

def right(i):
	return 2 * i + 2

def parent(i):
	return (i - 1) / 2

class tree(object):
        def __init__(self, lst):
                self.lst = lst[:]

        def inorder_tree_walk(self,x):
                if 0<= x < len(self.lst):
                        self.inorder_tree_walk(left(x))
                        print self.lst[x]
                        self.inorder_tree_walk(right(x))

        def inorder_tree_walk_stack(self, x):
                stack = []
                while 0 <= x < len(self.lst) or len(stack) > 0:
                        if 0 <= x < len(self.lst):
                                stack.append(x)
                                x = left(x)
                        else:
                                x = stack.pop(-1)
                                print self.lst[x]
                                x = right(x)
        
        def tree_search(self, i, k):
                if i < 0 or i >= len(self.lst):
                        return None
                if k == self.lst[i]:
                        return i
                if k < self.lst[i]:
                        return self.tree_search(left(i), k)
                else:
                        return self.tree_search(right(i), k)
        
        def tree_search_iterative(self, i, k):
                while 0 <= i < len(self.lst) and self.lst[i] != k:
                        if k < self.lst[i]:
                                i = left(i)
                        else:
                                i = right(i)
                if 0 <= i < len(self.lst):
                        return i
                else:
                        return None

        def tree_minimum(self, i):
                while 0 <= left(i) < len(self.lst):
                        i = left(i)
                return self.lst[i]
        
        def tree_maximum(self, i):
                while 0 <= right(i) < len(self.lst):
                        i = right(i)
                return self.lst[i]

if __name__ == "__main__":
        lst = [6,5,7,2,5,None,8]
        t = tree(lst)
        print "recursive"
        t.inorder_tree_walk(0)
        print "nonrecursive"
        t.inorder_tree_walk_stack(0)
        print "search 8"
        print t.tree_search(0, 8)
        print "search 9"
        print t.tree_search(0, 9)
        print "iter search 8"
        print t.tree_search_iterative(0, 8)
        print "iter search 9"
        print t.tree_search_iterative(0, 9)
        
        print "minimum is", t.tree_minimum(0)
        print "maximum is", t.tree_maximum(0)




