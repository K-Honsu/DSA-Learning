'''
stack operation include 
- create stack 
- push
- pop
- peek
- isEmpty
- isFull
- deleteStack
'''
# creating stack with size limit


class Stack:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return  '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return 'Stack is empty'
        return False
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    
    def push(self,value):
        if self.isFull():
            return 'Sorry cannot add items because stack is full'
        else:
            self.list.append(value)
            return self.list
        
    def pop(self):
        if self.isEmpty():
            return 'There are no elements in the stack'
        else:
            self.list.pop()
            
    def peek(self):
        if self.isEmpty():
            return 'There are no elements in the stack'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = []
        return self.list
        
        
customStack= Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(6)
customStack.push(9)
customStack.push(10)
customStack.pop()
# customStack.push(10)
print(customStack.peek())
customStack.delete()
print(customStack.peek())
print(customStack)