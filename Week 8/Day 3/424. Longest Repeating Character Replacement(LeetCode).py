# March 19 2025
# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        res = 0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r],0) + 1
            h = max(dic, key = dic.get)
            if (r - l) + 1 > dic[h] + k:
                dic[s[l]] -= 1
                l += 1
            print(r,l)
            res = max(res, (r - l) + 1)
        return res