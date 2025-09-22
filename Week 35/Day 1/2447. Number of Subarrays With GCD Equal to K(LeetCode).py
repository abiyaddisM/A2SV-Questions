# September 22 2025
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % k != 0:
                continue
            g = 0
            for j in range(i, n):
                if nums[j] % k != 0:
                    break
                g = gcd(g, nums[j])
                if g == k:
                    res += 1
                elif g < k:
                    break
        return res