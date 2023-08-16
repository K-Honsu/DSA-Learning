'''
queue operation include 
- create queue 
- Enqueue
- Dequeue
- peek
- isEmpty
- isFull
- deleteQueue
'''
# creating queue without size limit

class Queue:
    def __init__(self) -> None:
        self.list = []
        
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return  ' '.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def enqueue(self, value):
        self.list.append(value)
        return self.list
    
    def dequeue(self):
        if self.isEmpty():
            return 'List is empty'
        else:
            return self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return f'List is empty -> {self.list}'
        else:
            return self.list[0]
    
    def delete(self):
        self.list = []
    
customQueue = Queue()
customQueue.enqueue(4)
customQueue.enqueue(5)
customQueue.enqueue(6)
print(customQueue)
print('------')
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)
    
    
        
    