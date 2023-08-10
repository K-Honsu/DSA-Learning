class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return f"Sorry. cannot insert {value} at index"
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index -1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        print('Sorry, no values in the list')
    
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail #.value
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current #.value
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        removed_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            removed_node.next = None
        self.length -= 1
        return removed_node
    
    def pop_last(self):
        last_node = self.tail
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
        self.tail = temp_node
        temp_node.next = None
        self.length -= 1
        return last_node
    
    def reverse(self):
        previous = None
        current = self.head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head, self.tail = self.tail, self.head
        
    def remove(self, index):
        if index == self.length -1 or index == -1:
            return self.pop_last()
        elif index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        else:
            prev_node = self.get(index -1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node       
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def getNthtoKthElement(self, n):
        pointer1 = self.head
        pointer2 = self.head
        
        for _ in range(n):
            if pointer2 is not None:
                pointer2 = pointer2.next
                
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.value
            

        
new_linked = LinkedList()
new_linked.insert(0,100)
new_linked.append(5)
new_linked.append(10)
new_linked.prepend(18)
new_linked.insert(1,11)
new_linked.insert(1,20)
new_linked.set_value(2,1000)
# new_linked.traverse()
# print(new_linked)
# new_linked.pop_first()
print(new_linked.getNthtoKthElement(5))
# new_linked.reverse()
print(new_linked)
# print(new_linked.remove(-1))
# print(new_linked.remove(-1))
# new_linked.delete_all()
# print(new_linked)
# print(new_linked.search(20))
# print(new_linked.get(-1))
