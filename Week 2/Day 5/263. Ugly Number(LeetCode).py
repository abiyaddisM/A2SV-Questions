# February 7 2025
# https://leetcode.com/problems/ugly-number/description/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
                continue
            elif n % 3 == 0:
                n /= 3
                continue
            elif n % 5 == 0:
                n /= 5
                continue
            return False

        return True