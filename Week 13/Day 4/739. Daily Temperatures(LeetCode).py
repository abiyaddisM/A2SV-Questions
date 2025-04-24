# April 24 2025
# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = []
        temp.reverse()
        for i in range(len(temp)):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            res.append(i - stack[-1] if stack else 0)
            stack.append(i)
        res.reverse()
        return res