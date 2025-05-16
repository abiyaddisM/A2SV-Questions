# May 16 2025
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(m):
            count = 0
            for c in candies:
                count += c // m
            return count >= k
        l = 1
        r = max(candies)
        res = 0
        while l <= r:
            m = (r + l) // 2
            if helper(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
