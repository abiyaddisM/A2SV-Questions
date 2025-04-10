# April 10 2025
# https://leetcode.com/problems/number-of-substrings-with-only-1s/
class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] != '1':
                l = r + 1
            res += r - l + 1

        return res % (10**9 + 7)