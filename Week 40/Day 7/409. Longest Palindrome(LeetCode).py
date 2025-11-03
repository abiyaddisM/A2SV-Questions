# November 2 2025
# https://leetcode.com/problems/longest-palindrome/description/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        res = 0
        dic = Counter(s)
        for k, v in dic.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                odd = True
        if odd:
            res += 1
        return res
