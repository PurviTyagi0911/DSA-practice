#Symmetric tree
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
root=Node(1)
two1=Node(2)
two2=Node(2)
three=Node(3)
four=Node(4)
root.left=two1
root.right=two2
two1.left=three
two1.right=four
two2.left=four
two2.right=three
class Solution(object):
    def isSymmetric(self, root):
        left=root.left
        right=root.right
        def mirror(left,right):
            if left ==right == None:
                return True
            elif left ==None or right == None:
                return False
            else:
                if left.val!=right.val:
                    return False
                a=mirror(left.left,right.right)
                b= mirror(left.right,right.left)
                if a==b==True:
                    return True
            return False
        return mirror(left,right)
            











ss=Solution()
print(ss.isSymmetric(root))