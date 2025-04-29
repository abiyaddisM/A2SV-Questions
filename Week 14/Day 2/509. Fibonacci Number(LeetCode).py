# April 29 2025
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def helper(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            return helper(n - 1) + helper(n - 2)
        return helper(n)