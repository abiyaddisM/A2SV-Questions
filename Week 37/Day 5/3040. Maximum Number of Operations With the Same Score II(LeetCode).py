# October 10 2025
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        dic = {}
        def helper(l, r, total):
            if l >= r:
                return 0
            if (l, r) in dic:
                return dic[(l, r)]
            res = 0
            if nums[l] + nums[r] == total:
                res = max(res, helper(l + 1, r - 1, total) + 1)
            if nums[l] + nums[l + 1] == total:
                res = max(res, helper(l + 2, r, total) + 1)
            if nums[r] + nums[r - 1] == total:
                res = max(res, helper(l, r - 2, total)  + 1)
            dic[(l, r)] = res
            return res


        t1 = helper(1, len(nums) - 2, nums[0] + nums[-1]) + 1
        t2 = helper(2, len(nums) - 1, nums[0] + nums[1]) + 1
        t3 = helper(0, len(nums) - 3, nums[-2] + nums[-1]) + 1
        return max(t1,t2,t3)
