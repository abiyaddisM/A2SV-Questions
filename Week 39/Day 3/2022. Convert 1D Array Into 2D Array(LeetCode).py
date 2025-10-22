# October 22 2025
# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = [ [0 for _ in range(n)] for _ in range(m)]
        c = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = original[c]
                c += 1
        return res