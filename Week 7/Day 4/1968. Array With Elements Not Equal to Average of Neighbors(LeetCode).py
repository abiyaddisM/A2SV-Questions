# March 13 2025
#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        for i in range(1,len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        for i in range(1,len(nums) - 1):
            if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums