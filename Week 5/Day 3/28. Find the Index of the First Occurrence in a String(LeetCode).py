# February 26 2025
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, hy: str, ne: str) -> int:
        for i in range(len(hy) - (len(ne) - 1)):
            if ne == hy[i:i + len(ne)]:
                return i
        return -1