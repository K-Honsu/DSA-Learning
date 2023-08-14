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
# creating stack without size limit


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return  '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        self.list.append(value)
        return self.list
    
    def pop(self):
        self.list.pop()
        return self.list
    
    def peek(self):
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
    
    
stk = Stack()
print(stk.push(12))
print(stk.push(21))
print(stk.push(10))
stk.isEmpty()
print(stk.pop())
print(stk.peek())
print(stk)

