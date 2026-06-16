class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singly_LL:
    def __init__(self):
        self.head=None
    def append(self, val):
        new_Node=Node(val)
        if self.head==None:
            self.head=new_Node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_Node
    def traversal(self):
        if self.head is None:
            print('empty list')
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=' -> ')
                curr=curr.next
    def insert_at(self,val,position):
        new_Node=Node(val)
        if position==0:
            self.head=new_Node.next
            self.head=new_Node
        else:
            current=self.head
            previous_node=None
            count=0
            while current is not None and count<position:
                previous_node=current
                current=current.next
                count+=1
            previous_node.next=new_Node
            new_Node.next=current
    def delete(self,val):
        temp=self.head
        if temp.val==val:
            self.head=temp.next
            del temp
            return
        else:
            found= False
            prev=None
            while temp is not None:
                if temp.val==val:
                    found=True
                    break
                prev=temp
                temp=temp.next
                if found:
                    prev.next=temp.next
                    del temp
                    return
                else:
                    print('not found')
sll=singly_LL()
sll.append(19)
sll.append(20)
sll.append(20.5)
sll.insert_at(13,2)
sll.delete(19)
sll.traversal()
