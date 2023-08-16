class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self) -> str:
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
        

class Queue:
    def __init__(self) -> None:
        self.list = LinkedList()
        
    def __str__(self) -> str:
        values = [str(x.value) for x in self.list]
        return ' '.join(values)
        
    def isEmpty(self):
        if self.list.head == None:
            return True
        else:
            return False
    
    def enqueue(self, value):
        node = Node(value)
        if self.list.head == None:
            self.list.head = node
            self.list.tail = node
        else:
            self.list.tail.next = node
            self.list.tail = node
            
    def dequeue(self):
        temp = self.list.head
        if self.isEmpty():
            return 'Queue is empty'
        else:
            self.list.head = self.list.head.next
            return temp.value
    
    def peek(self):
        if self.isEmpty():
            return 'Nothing to look at here cause queue is empty'
        else:
            return self.list.head.value
        
    def delete(self):
        self.list.head , self.list.tail = None, None
        

queueLinkedList = Queue()
queueLinkedList.enqueue(10)
queueLinkedList.enqueue(19)
queueLinkedList.enqueue(23)
print('-----')
print(queueLinkedList.dequeue())
print(queueLinkedList.dequeue())
print('-----')
print(queueLinkedList.peek())
print(queueLinkedList.delete())
print(queueLinkedList)
            