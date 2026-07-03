class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class linked_list:
    def __init__(self):
        self.head=None
    def show(self):
        if self.head is None:
            print("linked_list is empty")
            return 
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.pointer
        print("None")
    def add(self,data):
        new_node=Node(data)
        temp=self.head
        if self.head is None:
            self.head=new_node
            return
        while temp.pointer:
            temp=temp.pointer
        temp.pointer=new_node
    def add_spec(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.pointer
        new_node.data=data
        new_node.pointer=temp.pointer
        temp.pointer=new_node
l=linked_list()
li=list(map(int,input().split(",")))
for i in li:
    l.add(i)
l.show()
l.add_spec(3,4)
l.show()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 