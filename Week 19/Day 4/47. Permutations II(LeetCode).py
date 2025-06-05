# June 5 2025
# https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            ms = set()
            for i in range(len(nums)):
                if not used[i] and nums[i] not in ms:
                    ms.add(nums[i])
                    used[i] = True
                    path.append(nums[i])

                    helper(path, used)
                    path.pop()
                    used[i] = False


        helper([], [False] * len(nums))
        return res