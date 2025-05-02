# May 2 2025
# https://leetcode.com/problems/maximum-width-ramp/description/
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1,len(nums)):
            if stack and nums[stack[-1]] > nums[i]:
                stack.append(i)
        res = 0
        for r in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[r]:
                l = stack.pop()
                res = max(res, r  - l )
        return res