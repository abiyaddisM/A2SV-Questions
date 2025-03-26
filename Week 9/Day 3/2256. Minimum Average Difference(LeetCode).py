# March 26 2025
# https://leetcode.com/problems/minimum-average-difference/
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        res = 0
        maxs = float('inf')
        for i in range(len(nums)):
            l = nums[i] // (i + 1)
            r = (nums[-1] - nums[i]) // (len(nums) - (i + 1)) if i < len(nums) - 1 else 0
            total = abs(l - r)
            res = i if total < maxs else res
            maxs = min(total,maxs)
        return res