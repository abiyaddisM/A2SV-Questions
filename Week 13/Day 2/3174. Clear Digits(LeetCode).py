# April 22 2025
# https://leetcode.com/problems/clear-digits/description/
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for n in s:
            if '0' <= n <= '9':
                stack.pop()
                continue
            stack.append(n)
        return ''.join(stack)