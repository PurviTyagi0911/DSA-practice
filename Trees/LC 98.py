#validate bst
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
root=Node(2) 
zero=Node(0)
one=Node(1)
root.left=one
root.right=zero
class Solution(object):
    def isValidBST(self, root):
        if root==None:
            return True
        if root.left!=None and root.left.val>=root.val:
            return False
        if root.right!=None and root.right.val<=root.val:
            return False
        a=self.isValidBST(root.left)
        b=self.isValidBST(root.right)
        if a == b== True:
            return True
        else:
            return False
ss=Solution()
print(ss.isValidBST(root))