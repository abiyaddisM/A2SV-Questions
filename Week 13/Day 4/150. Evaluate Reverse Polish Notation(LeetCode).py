# April 24 2025
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tok: List[str]) -> int:
        stack = []
        ms = {'+','-','*','/'}
        for i in range(len(tok)):
            if tok[i] not in ms:
                stack.append(int(tok[i]))
                continue
            m1 = stack.pop()
            m2 = stack.pop()
            if tok[i] == '+':
                stack.append(m2 + m1)
            elif tok[i] == '-':
                stack.append(m2 - m1)
            elif tok[i] == '*':
                stack.append(m2 * m1)
            else:
                stack.append(int(m2 / m1))
        return stack[-1]