# May 6 2025
# https://leetcode.com/problems/power-of-three/description/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n / 3)