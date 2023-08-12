from interview import LinkedList

def removenthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    
    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


customLL = LinkedList()
customLL.generate(10, 0,99)
print(customLL)
print(removenthToLast(customLL, 2))