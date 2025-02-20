# February 20 2025
# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bi = len(bin(num)) - 2
        return num ^ (2 ** bi - 1)