# April 13 2025
# https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution:
    def partitionString(self, s: str) -> int:
        ms = set()
        res = 1
        for i in range(len(s)):
            if s[i] in ms:
                res += 1
                ms.clear()
            ms.add(s[i])
        return res