# July 18 2025
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1
        for c in coins:
            if c != 1 and c > res:
                break
            res += c
        return res