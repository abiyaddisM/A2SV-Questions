# March 28 2025
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {}
        res = 0
        dic[0] = 1
        total = 0
        for n in nums:
            total += n
            if total % k in dic:
                res += dic[total % k]
            dic[total] = dic.get(total, 0) + 1
            if total >= k or total < 0:
                dic[total % k] = dic.get(total % k, 0) + 1
        return res