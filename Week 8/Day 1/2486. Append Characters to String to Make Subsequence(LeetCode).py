# March 17 2025
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = 0
        r = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                r += 1
            l += 1
        return len(t) - r