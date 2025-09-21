# September 21 2025
# https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        temp = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
        res = [ [0 for i in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = temp.popleft()
        return res
