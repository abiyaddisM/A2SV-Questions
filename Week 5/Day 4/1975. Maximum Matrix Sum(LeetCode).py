# February 27 2025
# https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, mat: List[List[int]]) -> int:
        total = 0
        mins = None
        count = 0
        isZero = False
        n = len(mat)
        for i in range(n):
            for j in range(n):
                total += abs(mat[i][j])
                if mat[i][j] == 0:
                    isZero = True
                if mat[i][j] < 0:
                    count += 1
                if not mins:
                    mins = abs(mat[i][j])
                    continue
                mins = min(mins,abs(mat[i][j]))
        if not isZero and count % 2 != 0:
            total -= mins * 2
        return total