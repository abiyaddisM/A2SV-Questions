# April 25 2025
# https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.stack = []
        self.mon = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mon or self.mon[-1] >= val:
            self.mon.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mon[-1]:
            self.mon.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mon[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()