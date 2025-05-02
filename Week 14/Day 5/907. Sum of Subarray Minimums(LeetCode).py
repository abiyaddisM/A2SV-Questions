# May 2 2025
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = []
        right = []
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left.append(i - (stack[-1] + 1) if stack else i)
            stack.append(i)
        stack = []
        for i in range(len(arr) - 1, -1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right.append(stack[-1] - (i + 1) if stack else (len(arr) - 1) - i)
            stack.append(i)
        right.reverse()
        res = []
        for i in range(len(arr)):
            l = 1 + left[i]
            r = 1 + right[i]
            t = l * r
            res.append(arr[i] * t)
        return sum(res) % (10 ** 9 + 7)