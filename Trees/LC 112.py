#path sum
targetSum=20
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False 
        targetSum-=root.val
        if root.left==None and root.right==None:
            return targetSum==0
        a=self.hasPathSum(root.left,targetSum)
        b=self.hasPathSum(root.right,targetSum)
        if a==True or b==True:
            return True
        return False
        



        
              





root=Node(5)
four=Node(4)
eight=Node(8)
eleven=Node(11)
thirteen=Node(13)
seven=Node(7)
two=Node(2)
one=Node(1)
root.left=four
root.right=eight
four.left=eleven
eight.left=thirteen
eight.right=four
four.right=one
ss=Solution()
print(ss.hasPathSum(root,targetSum))

