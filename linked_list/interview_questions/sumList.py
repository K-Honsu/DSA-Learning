from interview import LinkedList

def sumList(lis1, lis2):
    n1 = lis1.head
    n2 = lis2.head
    carry = 0
    ll = LinkedList()
    
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
    ll.addToBack(int(result % 10))
    carry = result / 10
        
    return ll

            
             