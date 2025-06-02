# June 2 2025
# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, can: List[int], tar: int) -> List[List[int]]:
        res = []
        def helper(can, arr = [], total = 0):
            if total == tar:
                res.append(arr)
            if total >= tar:
                return
            for i in range(len(can)):
                copy = arr[:]
                copy.append(can[i])
                helper(can[i:], copy, total + can[i])

        helper(can)
        return res