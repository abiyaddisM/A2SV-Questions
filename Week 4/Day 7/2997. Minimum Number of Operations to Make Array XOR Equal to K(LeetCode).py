# February 23 2025
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res = res ^ nums[i]
        br = bin(res)
        bk = bin(k)
        res = 0
        for i in range(max(len(br),len(bk))  - 2):
            top = br[-(i + 1)] if i < len(br) - 2 else '0'
            bottom = bk[-(i + 1)] if i < len(bk) - 2 else '0'
            if top != bottom:
                res += 1
        return res