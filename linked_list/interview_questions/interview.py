from random import randint
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
    
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
    
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        current = self.head
        while current:
            yield current
            result += 1
            current = current.next
        return result
    
    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode1 = Node(value)
            self.tail.next = newNode1
            self.tail = newNode1
            
    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_value,max_value))
        return self
    
    
    
currentLL = LinkedList()
currentLL.generate(10,0,99)
print(currentLL)