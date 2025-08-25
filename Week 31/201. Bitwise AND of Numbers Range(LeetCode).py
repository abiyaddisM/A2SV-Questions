# August 25 2025
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

