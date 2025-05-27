# May 27 2025
# https://leetcode.com/problems/find-the-middle-index-in-array/description/
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        for i in range(len(nums)):
            left = nums[i - 1] if i != 0 else 0
            right = nums[-1] - nums[i] if i != len(nums) - 1 else 0
            if left == right:
                return i

        return -1