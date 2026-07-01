#Same Tree
p = [1,2,3]
q = [1,2,3]
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
p=Node(1)
two=Node(2)
three=Node(3)
p.left=two
p.right=three
q=Node(1)
two=Node(2)
three=Node(3)
q.left=two


class Solution(object):
    def isSameTree(self, p, q):
        if p==q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val!=q.val:
            return False
        else:
            a=self.isSameTree(p.left,q.left)
            b=self.isSameTree(p.right,q.right)
            if a==b==True:
                return True
        return False
        
ss=Solution()
print(ss.isSameTree(p,q))