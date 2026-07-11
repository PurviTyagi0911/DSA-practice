#validate bst
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
root=Node(2) 
zero=Node(3)
one=Node(1)
root.left=one
root.right=zero
class Solution(object):
    min=-10
    max=0
    def isValidBST(self, root):
        def dfs(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))
        return dfs(root, float("-inf"), float("inf"))

ss=Solution()
print(ss.isValidBST(root))