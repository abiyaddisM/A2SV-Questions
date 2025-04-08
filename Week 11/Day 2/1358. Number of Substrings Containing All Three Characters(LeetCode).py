# April 8 2025
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        dic = {}
        l = 0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            res += l
            while len(dic) == 3:
                res += 1
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l += 1
        return res