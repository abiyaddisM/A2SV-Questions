# May 12 2025
# https://leetcode.com/problems/baseball-game/description/
class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack = []

        for o in op:
            if o not in ("C", "D", "+"):
                stack.append(int(o))
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)