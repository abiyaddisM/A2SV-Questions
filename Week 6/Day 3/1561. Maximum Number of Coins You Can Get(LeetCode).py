# March 5 2025
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        for i in range(len(piles) // 3):
            t = i + 1
            res += piles[len(piles) - (t * 2)]
        return res