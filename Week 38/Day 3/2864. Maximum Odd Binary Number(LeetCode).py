# October 15 2025
# https://leetcode.com/problems/maximum-odd-binary-number/description/
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        t1 = s.count('1')
        t2 = s.count('0')
        t1 -= 1
        res = '1' * t1
        res += '0' * t2
        return res + '1'