# February 24 2025
# https://leetcode.com/problems/largest-perimeter-triangle/description/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        for i in range(len(nums) - 2):
            a,b,c = nums[i],  nums[i + 1],  nums[i + 2]
            s = a + b + c
            m = max([a,b,c])
            if s > m * 2:
                return s
        return 0