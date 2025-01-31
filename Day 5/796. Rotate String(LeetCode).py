#January 31 2025
#https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = list(s)
        for i in range(len(s)):
            if ''.join(temp) == goal:
                return True
            t = temp[-1]
            for j in range(len(s)):
                temp[j], t = t, temp[j]
        return False

