#January 31 2025
#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left,right = len(s) - 1, len(s) - 1
        while left >= 0 and s[left] == " ":
            left -= 1
            right = left
        while left >= 0 and s[left] != " ":
            left -= 1
        return abs(right - left)
