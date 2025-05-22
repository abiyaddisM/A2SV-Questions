# May 22 2025
# https://leetcode.com/problems/backspace-string-compare/description/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(word):
            stack = []
            for s in word:
                if s == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s)
            return ''.join(stack)
        return helper(s) == helper(t)
