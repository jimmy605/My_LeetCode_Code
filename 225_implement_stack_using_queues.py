class MyStack:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        return self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return True if len(self.s1) == 0 else False 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()