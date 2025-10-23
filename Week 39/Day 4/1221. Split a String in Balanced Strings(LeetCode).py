# October 23 2025
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = 0
        r_count = 0
        res = 0
        for n in s:
            if n == 'R':
                r_count += 1
            if n == 'L':
                l_count += 1
            if r_count == l_count:
                res += 1
                l_count = 0
                r_count = 0

        return res