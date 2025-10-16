# October 16 2025
# https://leetcode.com/problems/matrix-diagonal-sum/description/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            j = -(i + 1)
            res += mat[i][i]
            res += mat[i][j]
        if n % 2 == 1:
            res -= mat[n // 2][n//2]
        return res