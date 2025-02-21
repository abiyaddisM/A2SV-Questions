# February 21 2025
# https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        row = set()
        col = set()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i in row or j in col:
                    mat[i][j] = 0        