# May 7 2025
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(m):
            s = 0
            for n in nums:
                s += math.ceil(n / m)
            return s
        l = 1
        r = max(nums)
        res = float('inf')
        while l <= r:
            m = (r + l) // 2
            val = helper(m)
            if val > threshold:
                l = m + 1
            else:
                r = m - 1
        return l
