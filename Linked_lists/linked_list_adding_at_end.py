class Node:
    # This is also for basic creation of linked lists
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list():
    def __init__(self):
        self.head=None
    def show(self):
        if self.head is None:
            return None
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
        print("None")
    def add(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
l=linked_list()
li=list(map(int,input().split(",")))
for i in li:
    l.add(i)
l.show()
