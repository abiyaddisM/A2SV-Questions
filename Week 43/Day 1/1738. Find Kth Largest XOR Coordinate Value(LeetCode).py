# November 17 2025
# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        vals = []

        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = (
                        pre[i][j + 1] ^
                        pre[i + 1][j] ^
                        pre[i][j] ^
                        matrix[i][j]
                )
                vals.append(pre[i + 1][j + 1])

        vals.sort(reverse=True)
        return vals[k - 1]
