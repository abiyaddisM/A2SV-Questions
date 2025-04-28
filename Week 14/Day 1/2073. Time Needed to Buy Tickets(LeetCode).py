# April 28 2025
# https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, ta: List[int], k: int) -> int:
        check = ta[k]
        res = 0
        for i in range(len(ta)):
            res += min(check if i <= k else check - 1, ta[i] )
        return res