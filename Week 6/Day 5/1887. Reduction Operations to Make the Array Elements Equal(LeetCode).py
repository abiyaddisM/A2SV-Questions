# March 7 2025
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                res += i
        return res