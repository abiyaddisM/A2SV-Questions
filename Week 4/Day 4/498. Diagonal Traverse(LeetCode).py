# February 20 2025
# https://leetcode.com/problems/diagonal-traverse/
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        flag = 1
        i = 0
        j = 0
        while i < len(mat) and j < len(mat[0]):
            res.append(mat[i][j])
            if flag:
                if j + 1 == len(mat[0]):
                    i += 1
                    flag = 0
                elif i - 1 < 0:
                    j += 1
                    flag = 0
                else:
                    j += 1
                    i -= 1
            else:
                if i + 1 == len(mat):
                    j += 1
                    flag = 1
                elif j - 1 < 0:
                    i += 1
                    flag = 1
                else:
                    j -= 1
                    i += 1


        return res