# April 28 2025
# https://leetcode.com/problems/132-pattern/description/
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')
        for n in reversed(nums):
            if n < third:
                return True
            while stack and stack[-1] < n:
                third = stack.pop()
            stack.append(n)
        return False