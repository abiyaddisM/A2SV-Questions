# November 14 2025
# https://leetcode.com/problems/maximum-gap/description/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1):
            res = max(res, nums[i + 1] - nums[i])
        return res