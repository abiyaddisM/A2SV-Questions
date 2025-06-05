# June 5 2025
# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, arr = []):

            for i in range(len(nums)):
                if nums[i] != '*':
                    arr.append(nums[i])
                    temp = nums[i]
                    nums[i] = '*'
                    helper(nums, arr)
                    arr.pop()
                    nums[i] = temp

            if len(arr) == len(nums):
                res.append(arr[:])

        helper(nums)
        return res