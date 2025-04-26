# April 25 2025
# https://leetcode.com/problems/score-of-parentheses/description/

class Solution:
    def scoreOfParentheses(self, arr: str) -> int:
        stack = []
        for s in arr:
            if s == '(':
                stack.append(0)
                continue
            total = 0
            while stack and stack[-1] != 0:
                total += stack[-1]
                stack.pop()
            stack.pop()
            stack.append(2 * total if total else 1)
        res = sum(stack)
        return res