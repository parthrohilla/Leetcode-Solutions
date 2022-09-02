class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        k = len(self.stack)
        for _ in range(k-1):
            self.temp.append(self.stack.pop())
        
        top = self.stack.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return top

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()