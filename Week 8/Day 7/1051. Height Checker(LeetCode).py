# March 23 2025
# https://leetcode.com/problems/height-checker/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        res = 0
        for i in range(len(temp)):
            if temp[i] != heights[i]:
                res += 1
        return res