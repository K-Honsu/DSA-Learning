class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return 'The node has been inserted'
    
    def insertAtBeginning(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.tail.next = self.head
        return 'New node appended'
    
    def insertAtEnd(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.tail.next = self.head
        return 'New node appended at end'
    
    def insertAtIIndexLocation(self, value, index):
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
            self.tail.next = node
        elif index == -1:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            # node.next = self.tail.next
            # self.tail.next = node
            # self.tail = node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
    
    def traverse(self):
        if self.head is None:
            return 'No values in the list'
        else:
            curr = self.head
            while curr:
                print(curr.value)
                curr = curr.next
                if curr == self.tail.next:
                    break
    
    def search(self, value):
        if self.head is None:
            return 'No values in the list'
        else:
            curr = self.head
            while curr:
                if curr.value == value:
                    print(f'Value found and value is {curr.value}')
                curr = curr.next
                if curr == self.tail.next:
                    return 'Value not found'
        
    def deleteNode(self,index):
        if self.head is None:
            return 'No value in the list'
        else:
            curr = self.head
            if index == 0:
                self.head = curr.next
                self.tail.next = self.head
            elif index == -1:
                while curr.next is not self.tail:
                    curr = curr.next
                self.tail = curr
                curr.next = None
                self.tail.next = self.head
            else:
                for _ in range(index -1):
                    curr = curr.next
                popped_node = curr.next
                curr.next = popped_node.next
                popped_node.next = None
                
                
    def deleteAllNode(self):
        self.head = None
        self.tail = None
        # self.tail.next = self.head
                

    def remove_duplicates(self, ll):
        obj = {}
        node = ll.head
        prev = None
        while node:
            if node.value in obj:
                if node.next is None:
                    self.tail = prev
                else:
                    prev.next = node.next
            else:
                obj[node.value] = True
                prev = node
            node = node.next
        return ll
    
    
    def getNthtoKthElement(self, n):
        pointer1 = self.head
        pointer2 = self.head
        
        for _ in range(n):
            if pointer2 is not None:
                pointer2 = pointer2.next
                
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
                    
        

node = CircularLinkedList()
node.create(1)
# node.insertAtBeginning(5)
# node.insertAtEnd(10)
node.insertAtIIndexLocation(11,-1)
node.insertAtIIndexLocation(44,0)
node.insertAtIIndexLocation(98,0)
node.insertAtIIndexLocation(13,0)
node.insertAtIIndexLocation(81,3)
# node.traverse()
print(node.search(0))
# print(node.deleteNode(2))
# node.deleteAllNode()
# node.remove_duplicates()
print(node.getNthtoKthElement(2))

print([node.value for node in node])