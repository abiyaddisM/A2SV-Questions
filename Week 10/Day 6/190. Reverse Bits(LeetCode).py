# April 5 2025
# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        print(bin(n))
        n = str(bin(n))
        res = ''
        for i in range(len(n) - 2):
            j = -(i + 1)
            res += n[j]
        res +=  '0' * (34 - len(n))
        return int(res, 2)