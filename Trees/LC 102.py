#Binary tree level order traversal
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
    def bfs(self,root):
        output=[]
        q=Queue()
        q.push(root)
        while q.values:
          size=len(q.values)
          curr_l=[]
          while size>0 :
              e=q.pop()
              curr_l.append(e.val)
              if e.left!=None:
                  q.push(e.left)
              if e.right!=None:
                  q.push(e.right)
              size-=1
              
          output.append(curr_l)

        return output




        
root=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
root.left=two
root.right=three
two.left=four
two.right=five
three.left=six
print(root.bfs(root))