#maximum depth of a tree
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    max_depth=0
    def depth(self,node):
        if node==None:
            return 0
        left_d=self.depth(node.left)
        right_d=self.depth(node.right)
        max_depth=1+max(left_d,right_d)
        return max_depth

three=Node(3)
nine=Node(9)
twenty=Node(20)
fifteen=Node(15)
seven=Node(7)
two=Node(2)

three.left=nine
three.right=twenty
twenty.left=fifteen
twenty.right=seven
seven.left=two
print(three.depth(three))
