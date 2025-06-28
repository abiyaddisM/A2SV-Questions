# June 27 2025
# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            if n % 2 != 0:
                res += 1
            n //= 2
        return res