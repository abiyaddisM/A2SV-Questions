# February 28 2025
# https://leetcode.com/problems/toeplitz-matrix/description/
class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        for t in range(len(mat[0]) - 1):
            i = 0
            j = t
            while i + 1 < len(mat) and j + 1 < len(mat[0]):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False
                i += 1
                j += 1
        for t in range(len(mat) - 1):
            i = t
            j = 0
            while i + 1 < len(mat) and j + 1 < len(mat[0]):
                if mat[i][j] != mat[i + 1][j + 1]:
                    return False
                i += 1
                j += 1


        return True