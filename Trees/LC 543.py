#diameter of binary tree
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
root=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
root.left=two

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans=0
        def dfs(root):
            if root==None:
               return 0
            left=dfs(root.left)
            right=dfs(root.right)
            height=max(left,right)+1
            self.ans=max(self.ans,left+right)
            return height 
        dfs(root)
        return self.ans
ss=Solution()
print(ss.diameterOfBinaryTree(root))
  