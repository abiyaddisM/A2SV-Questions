# April 30 2025
# https://leetcode.com/problems/powx-n/description/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            return self.myPow(x, n - 1) * x