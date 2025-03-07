# March 7 2025
# https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            r = s[0:i]
            l = s[i:len(s)]
            if l + r == goal:
                return True


        return False