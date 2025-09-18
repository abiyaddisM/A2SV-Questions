# September 18 2025
# https://leetcode.com/problems/combination-sum-iv/description/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dic = {}
        def helper(t):
            if t == 0:
                return 1
            if t < 0:
                return 0
            if t in dic:
                return dic[t]
            temp = 0
            for n in nums:
                temp += helper(t - n)
            dic[t] = temp
            return temp

        return helper(target)