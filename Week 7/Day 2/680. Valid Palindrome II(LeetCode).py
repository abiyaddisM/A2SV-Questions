# March 11 2025
# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            flag = False
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    if flag:
                        return False
                    l += 1
                    flag = True
                    continue
                l += 1
                r -= 1
            return True
        return helper(s) or helper(s[::-1])