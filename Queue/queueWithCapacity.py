class Queue:
    def __init__(self, maxSize) -> None:
        self.list = maxSize + [None]
        self.maxSize = maxSize
        self.start = -1
        self.end = -1
        
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isFull(self):
        if self.end + 1 == self.start:
            return True
        elif self.start == 0 and self.end + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.end == -1:
            return True
        else:
            return False