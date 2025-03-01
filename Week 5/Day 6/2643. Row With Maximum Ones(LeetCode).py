# March 1 2025
# https://leetcode.com/problems/row-with-maximum-ones/description/
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = [0,0]
        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    c += 1
            if c > count[1]:
                count[0] = i
                count[1] = c
        return count