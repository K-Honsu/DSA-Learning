# creating a stack with LinkedList
class Node:
    def __init__(self,value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __iter__(self) -> str:
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Stack:
    def __init__(self) -> None:
        self.linkedList = LinkedList()
        
    def __str__(self) -> str:
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)
        
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        return False
    
    def push(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedList.head = node
        else:
            node.next = self.linkedList.head
            self.linkedList.head = node
            
    def pop(self):
        if self.linkedList.head == None:
            return 'Nothing to remove because stack is head is None'
        else:
            self.linkedList.head = self.linkedList.head.next
            # self.linkedList.head.next = None
            return self.linkedList
        
    def peek(self):
        if self.isEmpty():
            return 'List is empty'
        return self.linkedList.head.value
    
    def delete(self):
        self.linkedList.head = None
    
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print('--------')
customStack.pop()
print(customStack.peek())
# customStack.delete()
print(customStack)