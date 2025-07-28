#January 29 2025
#https://leetcode.com/problems/isomorpthic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        ms = set()
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False

            else:
                if t[i] in ms:
                    return False
                ms.add(t[i])
                dic[s[i]] = t[i]
        return True