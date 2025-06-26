# June 25 2025
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        memo = [[-1 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]

        def helper(row, col):
            if memo[row][col] != -1:
                return memo[row][col]
            temp = 1
            for dx, dy in dir:
                cx = row + dx
                cy = col + dy
                if inbound(cx, cy) and matrix[row][col] < matrix[cx][cy]:
                    t = helper(cx, cy)
                    temp = max(t + 1, temp)
                    memo[cx][cy] = t

            return temp

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if memo[i][j] == -1:
                    res = max(res, helper(i, j))
        return res
