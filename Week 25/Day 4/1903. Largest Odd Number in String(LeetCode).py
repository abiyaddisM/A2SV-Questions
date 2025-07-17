# July 15 2025
# https://leetcode.com/problems/largest-odd-number-in-string/description/
class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        for i in range(len(num)):
            if int(num[i: i + 1]) % 2 == 1:
                res = num[: i + 1]
        return res
