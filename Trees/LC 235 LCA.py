#LCA of binary search tree
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
p=2
q=4
root=Node(6)
two=Node(2)
eight=Node(8)
zero=Node(0)
four=Node(4)
seven=Node(7)
nine=Node(9)
three=Node(3)
five=Node(5)
root.left=two
root.right=eight
two.left=zero
two.right=four
eight.left=seven
eight.right=nine
four.left=three
four.right=five
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val<p and root.val<q:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val>p and root.val>q:
            return self.lowestCommonAncestor(root.left,p,q)

        else:
            return root.val
ss= Solution()
print(ss.lowestCommonAncestor(root,p,q))


        