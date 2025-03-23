# March 23 2025
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
class Solution:
    def minimumRecolors(self, b: str, k: int) -> int:
        res = k
        total = 0
        l = 0
        for r in range(len(b)):
            if b[r] == 'W':
                total += 1
            if r + 1 >= k:
                res = min(res,total)
                if b[l] == 'W':
                    total -= 1
                l += 1
        return res