# April 11 2025
# https://leetcode.com/problems/trapping-rain-water/description/?envType=problem-list-v2&envId=two-pointers
class Solution:
    def trap(self, h: List[int]) -> int:
        # res = 0
        # stack = []
        # index = []
        # for i in range(len(h)):
        #     total = 0
        #     while len(stack) > 0 and stack[-1] < h[i]:
        #         index.pop()
        #         stack.pop()
        #     stack.append(h[i])
        #     index.append(i)
        # return res
        res = 0
        left = [0]
        right = [0]
        for i in range(len(h)):
            j = -(i + 1)
            left.append(max(left[i],h[i]))
            right.append(max(right[i],h[j]))
        right.reverse()
        for i in range(1, len(left)):
            m = min(left[i],right[i - 1])
            res += m - h[i - 1]
        return res