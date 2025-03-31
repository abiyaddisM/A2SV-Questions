# March 31 2025
# https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        dic[0] = 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dic:
                res += dic[total - k]
            dic[total] = dic.get(total, 0) + 1
        return res