class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Singly_LL:
    def __init__(self):
        self.head=None
    def appendd_at_pos(self,val,position):
        new_Node=Node(val)
        if position==0:
            new_Node.next=self.head
            self.head=new_Node
        else:
            previous=None
            curr=self.head
            count=0
            while curr is not None and count<position:    
                previous=curr
                curr=curr.next
                count+=1
            previous.next=new_Node
            new_Node.next=curr
    def appendd(self,val):
        new_Node=Node(val)
        if self.head==None:
            self.head=new_Node
        else:
          current=self.head
          while current.next is not None:
            current=current.next
          current.next=new_Node
    def length(self):
        current=self.head
        count=0
        while current is not None:
            current=current.next
            count+=1
        return count
    def mid_val(self):
        count= self.length()
        if count%2!=0:
          mid=count//2
        else:
            mid=count//2
        i=0
        curr=self.head
        while i<mid:
            curr=curr.next
            i+=1
        return curr.val
    def rev_list(self):
        previous=None
        curr=self.head
        next_node=None
        while curr is not None:
            next_node=curr.next
            curr.next=previous
            previous=curr
            curr=curr.next
        return previous.val
    def hasCycle(self):
       fast_curr=self.head
       slow_curr=self.head
       while fast_curr.next is not None and fast_curr.next.next is not None:
          fast_curr=fast_curr.next.next
          slow_curr=slow_curr.next
          if fast_curr==slow_curr:
            return True
            break
       return False




        


sll=Singly_LL()
sll.appendd(1)
sll.appendd(2)
sll.appendd(3)
sll.appendd(4)
sll.appendd(5)
#sll.appendd(6)
print(sll.hasCycle())
