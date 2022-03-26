class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp_stack = []
    
    def push(self, x: int) -> None:
        # If no elements are on the stack add it to stack
        if len(self.stack) == 0:
            self.stack.append(x)
        else:
            # While elements are on the stack move them temporarly onto temp_stack
            while self.stack:
                self.temp_stack.append(self.stack.pop())
            # Add the pushed item to the stack once all existing elements are moved to the temp_stack
            self.stack.append(x)
            # Add the temp_stack items back onto stack
            while self.temp_stack:
                self.stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()