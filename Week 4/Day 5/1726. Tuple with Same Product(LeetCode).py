# February 21 2025
# https://leetcode.com/problems/tuple-with-same-product/description/
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                t = nums[i] * nums[j]
                dic[t] = dic.get(t, 0) + 1

        for k, v in dic.items():
            if v > 1:
                res += (v * (v - 1) // 2) * 8

        return res