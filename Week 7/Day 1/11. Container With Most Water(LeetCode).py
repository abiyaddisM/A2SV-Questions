# March 10 2025
# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, he: List[int]) -> int:
        res = 0
        l = 0
        r = len(he) - 1
        while r > l:
            h = min(he[r], he[l])
            w = r - l
            res = max(res, h * w)
            if he[r] >= he[l]:
                l += 1
            else:
                r -= 1

        return res