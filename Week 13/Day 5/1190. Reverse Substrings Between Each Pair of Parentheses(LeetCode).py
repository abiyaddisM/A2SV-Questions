# April 25 2025
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
class Solution:
    def reverseParentheses(self, arr: str) -> str:
        stack = []
        letter = ''
        for s in arr:
            if s == '(':
                if letter:
                    stack.append(letter)
                    letter = ''
                stack.append('(')
                continue
            if s != ')':
                letter += s
                continue
            while stack and stack[-1] != '(':
                letter = stack.pop() + letter
            stack.pop()
            stack.append(letter[::-1])
            letter = ''
        res = ''
        for s in stack:
            res += s
        res += letter
        return res