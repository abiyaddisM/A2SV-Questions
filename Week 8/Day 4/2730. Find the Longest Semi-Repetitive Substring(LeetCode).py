# March 20 2025
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        res = 0
        l = 0
        adj = 0
        for r in range(1,len(s)):
            if s[r - 1] == s[r]:
                adj += 1
            while l != r and adj > 1:
                if s[l] == s[l + 1]:
                    adj -= 1
                l += 1
            res = max(res, (r - l) + 1)
        return res