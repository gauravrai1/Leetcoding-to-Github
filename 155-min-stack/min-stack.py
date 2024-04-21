class MinStack:

    def __init__(self):
        self.stack = []
        self.minv = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minv) == 0 or self.minv[-1] > val:
            self.minv.append(val)

    def pop(self) -> None:
        popv = self.stack.pop()
        if popv == self.minv[-1]:
            self.minv.pop()
            if popv in self.stack:
                self.minv.append(popv)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minv[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()