#invert binary tree
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
root=Node(4)
two=Node(2)
seven=Node(7)
one=Node(1)
three=Node(3)
six=Node(6)
nine=Node(9)
eight=Node(8)
root.left=two
root.right=seven
two.left=one
two.right=nine
seven.left=six
seven.right=nine

print(root.left.val,root.right.val)
class Solution(object):
    def invertTree(self, root):
        if root==None:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

ss=Solution()
print(ss.invertTree(root))
