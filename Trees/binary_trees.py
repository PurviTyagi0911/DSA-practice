class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def preorder(self,node):
        if node==None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)
    def inorder(self,node):
        if node==None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)
    def postorder(self,node):
        if node==None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)

drinks=Node('drinks')
root=drinks
hot = Node('hot')
cold= Node('cold')
tea=Node('coffee')
cola=Node('cola')
drinks.left=hot
drinks.right=cold
hot.left=tea
cold.left=cola
root.preorder(root)
print('/')
root.inorder(root)
print('/')
root.postorder(root)


