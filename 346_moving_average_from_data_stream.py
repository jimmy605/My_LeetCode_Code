class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.queue = []

    def next(self, val: int) -> float:
        L = len(self.queue)
        
        if L < self.size:
            self.queue.append(val)
            return sum(self.queue) / len(self.queue)
        
        else:
            self.queue = self.queue[1:]
            self.queue.append(val)
            return sum(self.queue) / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
test = MovingAverage(5)
for num in [[12009],[1965],[-940],[-8516],[-16446],[7870],[25545],[-21028],[18430],[-23464]]:
    print(test.next(num[0]), end='  ')
