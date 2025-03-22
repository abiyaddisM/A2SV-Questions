# March 22 2025
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        l = 0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            while dic[s[r]] == 2:
                dic[s[l]] -= 1
                l += 1
            res = max(res,r - l + 1)
        return res