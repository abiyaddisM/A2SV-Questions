# April 29 2025
# https://leetcode.com/problems/power-of-four/description/
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helper(n):
            if n == 1:
                return True
            if n < 1 or n % 4 != 0:
                return False
            return helper(n // 4)
        return helper(n)