# February 21 2025
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            if len(grid) - i < 3:
                break
            for j in range(len(grid[i])):
                if len(grid[i]) - j < 3:
                    break
                t = grid[i + 1][j + 1]
                for k in range(3):
                    t += grid[i][j + k]
                    t += grid[i + 2][j + k]
                res = max(res,t)
        return res