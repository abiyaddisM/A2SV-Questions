# June 3 2025
# https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(s='', open=0, close=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open < n:
                helper(s + '(', open + 1, close)
            if close < open:
                helper(s + ')', open, close + 1)
        helper()
        return res