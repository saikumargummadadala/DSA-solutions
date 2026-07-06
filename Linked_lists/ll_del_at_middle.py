class node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class ll:
    def __init__(self):
        self.head=None
    def show(self):
        temp=self.head
        if self.head==None:
            return
        while temp:
            print(temp.data,end=" ")
            temp=temp.pointer
    def add(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            return
        temp=self.head
        while temp.pointer:
            temp=temp.pointer
        temp.pointer=new_node
    def del_at_middle(self):
        if self.head is None:
            return 
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.pointer
        pos=count//2
        temp=self.head.pointer
        prev=self.head
        for i in range(1,pos):
            temp=temp.pointer
            prev=prev.pointer
        prev.pointer=temp.pointer
        temp.pointer=None
l=ll()
li=[10,20,30,40,50]
for i in li:
    l.add(i)
l.show()
print()
#middle element will be deleted 
l.del_at_middle()
l.show()