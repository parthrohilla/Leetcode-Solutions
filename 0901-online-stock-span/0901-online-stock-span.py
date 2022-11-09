class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price,1])
            return 1
        else:
            if price < self.stack[-1][0]:
                self.stack.append([price,1])
                return 1
            else:
                temp = 1
                while self.stack and self.stack[-1][0] <= price:
                    temp += self.stack[-1][1]
                    self.stack.pop()
                self.stack.append([price,temp])
                return temp


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)