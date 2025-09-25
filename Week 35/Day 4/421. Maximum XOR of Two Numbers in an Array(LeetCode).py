# September 25 2025
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        W = max(nums).bit_length() if nums else 1

        root = {}
        def insert(x: int) -> None:
            cur = root
            for k in range(W - 1, -1, -1):
                b = (x >> k) & 1
                if b not in cur:
                    cur[b] = {}
                cur = cur[b]

        def best_xor_with(x: int) -> int:
            cur = root
            ans = 0
            for k in range(W - 1, -1, -1):
                b = (x >> k) & 1
                want = 1 - b
                if want in cur:
                    ans |= (1 << k)
                    cur = cur[want]
                else:
                    cur = cur[b]
            return ans

        res = 0
        insert(nums[0])
        for i in range(1, len(nums)):
            res = max(res, best_xor_with(nums[i]))
            insert(nums[i])
        return res