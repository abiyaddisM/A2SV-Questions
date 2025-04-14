# April 13 2025
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            res = max(res,nums[r] + nums[l])
            l += 1
            r -= 1

        return res