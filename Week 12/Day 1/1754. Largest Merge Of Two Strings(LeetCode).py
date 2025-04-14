# April 14 2025
# https://leetcode.com/problems/largest-merge-of-two-strings/description/
class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        res = ''
        l = 0
        r = 0
        while l < len(w1) or r < len(w2):
            if w1[l:] > w2[r:]:
                res += w1[l]
                l += 1
            else:
                res += w2[r]
                r += 1
        return res