import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class Linked_list:
    def __init__(self):
        self.head=None
    def show(self):
        if self.head is None:
            return ("Linked list is empty")
        temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.pointer
        print("None")
    def add_at_beginning (self,data):
        new_node=Node(data)
        new_node.pointer=self.head
        self.head=new_node
l=Linked_list()
li=list(map(sys.stdin.read().split(",")))
#li=[10,20,30,40]
for i in li:
    l.add_at_beginning(i)
l.show()