# April 22 2025
# https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for n in s:
            if n == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(n)
        return ''.join(stack)