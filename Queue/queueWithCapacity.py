class Queue:
    def __init__(self, maxSize) -> None:
        self.list = maxSize + [None]
        self.maxSize = maxSize
        self.start = -1
        self.end = -1
        
    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return ' '.join(values)