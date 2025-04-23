# April 23 2025
# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        s1 = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for n in s:
            if n in s1:
                stack.append(n)
            else:
                if not stack or s1[stack[-1]] != n:
                    return False
                stack.pop()
        return len(stack) == 0
