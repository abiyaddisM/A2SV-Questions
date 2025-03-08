# March 8 2025
# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        c = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                c += 1
            if c == 2:
                return nums[i]
        return nums[0]