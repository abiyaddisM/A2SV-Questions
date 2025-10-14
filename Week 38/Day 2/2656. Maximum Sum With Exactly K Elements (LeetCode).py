# October 14 2025
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        res = 0

        for _ in range(k):
            res += m
            m += 1
        return res