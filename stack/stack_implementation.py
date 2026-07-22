class stack:
    def __init__(self):#implemets the empty list for stack implementation 
        self.elements=[]
    def is_empty(self):#argument for checking whether the stack is empty or not 
        return len(self.elements) == 0
    def push(self,element):#adding or pushing elements in to a stack
        self.elements.append(element)
    def pop(self):#dleting or poping elements at the top 
        if self.is_empty():
            raise IndexError("the stack is empty cant use pop")
        else:
            return self.elements.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.elements[-1]
    def size(self):
        return len(self.elements)
s=stack()
arr=[10,20,30,40,50]
for i in arr:
    s.push(i)
print("Stack after push:",s.elements)#prints the pushed elements in the stack 
print("traverses stack's top element",s.peek())
print("The stack is empty:",s.is_empty())
print("The size of stack:",s.size())
print("popped item:",s.pop())
print("Stack after poped:",s.elements)
