# February 13 2025
# https://leetcode.com/problems/separate-black-and-white-balls/description/
class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        count = 0
        for i in range(len(s)):
            if s[i] == '0':
                res += (i - count)
                count += 1
        return res