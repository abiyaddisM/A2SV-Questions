# June 17 2025
# https://leetcode.com/problems/arithmetic-subarrays/description/
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        def isArith(nums):
            for i in range(1,len(nums) - 1):
                if nums[i] - nums[i - 1] != nums[i + 1] - nums[i]:
                    return False
            return True
        for i in range(len(l)):
            res.append(isArith(sorted(nums[l[i] : r[i] + 1])) )
        return res