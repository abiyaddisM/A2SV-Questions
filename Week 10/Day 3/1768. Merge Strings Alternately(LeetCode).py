# April 2 2025
# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res = ''
        for i in range(len(w1)):
            res += w1[i]
            if i < len(w2):
                res += w2[i]
        if len(w1) < len(w2):
            res += w2[len(w1):]
        return res