class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def show(self):
        if self.head is None:
            print("linked_list is empty")
        
        else:
            temp=self.head
            while temp:
                x=temp.data
                temp=temp.next
                print(x,"-->",end="")
    def add(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def middle(self):
        if self.head is None:
            return None
        #implementation of fast and slow pointers 
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       return slow.data
l=linkedlist()
li=list(map(int,input().split(",")))
for i in li:
    l.add(i)
l.show()
print()
print(l.middle())
