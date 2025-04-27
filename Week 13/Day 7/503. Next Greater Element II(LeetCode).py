# April 27 2025
# https://leetcode.com/problems/next-greater-element-ii/description/
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nums.reverse()
        for n in nums:
            while stack and stack[-1] < n:
                stack.pop()
            stack.append(n)
        res = []
        for n in nums:
            while stack and stack[-1] <= n:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(n)
        res.reverse()
        return res