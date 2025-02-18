# February 18 2025
# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        res = []
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                res.append(nums[i])
        res.extend([0 for _ in range(c)])
        return res