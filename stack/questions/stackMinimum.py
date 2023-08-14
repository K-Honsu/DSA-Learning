class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value