# March 30 2025
# https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        res = 0
        total = 0
        l = 0
        r = len(p) - 1
        while l <= r:
            if p[r] + p[l] <= limit or p[r] > limit:
                res += 1
                l += 1
            elif p[r] <= limit:
                res += 1
            r -= 1

        return res