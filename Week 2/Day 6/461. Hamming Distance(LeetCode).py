# February 8 2025
# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)
        y = bin(y)
        res = 0
        size = max(len(x),len(y))
        for i in range(1,size - 1):
            xind = x[-i] if i < len(x) - 1 else '0'
            yind = y[-i] if i < len(y) - 1 else '0'
            if yind != xind:
                res += 1
            print(xind,yind)
        return res