# November 1 2025
# https://leetcode.com/problems/fibonacci-number/description/
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)