from interview import LinkedList

def partition(ll, x):
    current = ll.head
    ll.tail = current
    
    while current:
        nextNode = current.next
        current.next = None
        
        if current.value <= x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current 
        current = nextNode 
        
    if ll.tail.next is not None:
        ll.tail.next = None
        
customLL = LinkedList()
customLL.generate(10, 0,20)
print(customLL)
partition(customLL, 10)
print(customLL)