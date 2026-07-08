class Queue:
    def __init__(self):
        self.values=[]
    def push(self,valu):
        self.values.append(valu)
    def pop(self):
        return self.values.pop(0)
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def bfs(self,node):
        result=[]
        q=Queue()
        q.push(node)
        while q.values:
            e=q.pop()
            result.append(e.val)
            if e.left!=None:
                q.push(e.left)
            if e.right!=None:
                q.push(e.right)
        return result
root=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
root.left=two
root.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
print(root.bfs(root))

    