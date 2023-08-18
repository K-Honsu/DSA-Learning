import pprint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
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
        
    def remove(self,index):
        current = self.head
        if index == 0:
            self.head = self.head.next
            current.next = None
        elif index == -1 or index == self.length -1:
            last_node = self.tail
            while current.next is not self.tail:
                current= current.next
            self.tail = current
            current.next = None
            self.length -= 1
            return last_node.value
        elif index >= self.length or index < 0:
            return None
        else:
            for _ in range(index -1):
                current = current.next
            popped_node = current.next
            
            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = current
                
            current.next = popped_node.next
            popped_node.next = None
            self.length -=1
            # print(self.length)
            return current.value
    
    def middle(self):
        if self.length > 0:
            len = self.length // 2
            print(len)
            current = self.head
            current_index = 0
            
            while current_index < len:
                current = current.next
                current_index += 1
            return current.value
    
    # def remove_duplicates(self):
    #     obj = {}
    #     current = self.head
    #     while current:
    #         current = current.next
    #         if current.value in obj:
    #             if current.next is None:
    #                 self.tail = current
    #             else:
    #                 current.next = current.next.next
    #         obj[current] = current
    
    def remove_duplicates(self):
        obj = {}
        current = self.head
        prev = None

        while current:
            if current.value in obj:
                # Duplicate found, skip this node
                if current.next is None:
                    self.tail = prev
                else:
                    prev.next = current.next
                    # current.next = None
            else:
                # Add current node's value to the obj dictionary
                obj[current.value] = True
                prev = current

            current = current.next
        # print(obj)
        # return prev.next
        while prev:
            print(prev)
            prev = prev.next

    

            
    
new_linked = LinkedList()
new_linked.append(23)
new_linked.append(12)
new_linked.append(20)
new_linked.append(30)
new_linked.append(30)
new_linked.append(40)
new_linked.append(30)
new_linked.append(80)
new_linked.append(100)
new_linked.append(80)
new_linked.append(90)

# print(new_linked.remove(2))
# print(new_linked.middle())
# print(new_linked.remove(2))
new_linked.remove_duplicates()
print(new_linked)

