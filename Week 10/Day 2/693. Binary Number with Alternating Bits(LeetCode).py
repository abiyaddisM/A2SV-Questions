# April 1 2025
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)
        for i in range(2, len(n) - 1):
            if n[i] == n[i + 1]:
                return False
        return True