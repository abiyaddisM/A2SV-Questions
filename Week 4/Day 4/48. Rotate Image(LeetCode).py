# February 20 2025
# https://leetcode.com/problems/rotate-image/description/
class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        count = 0
        n = len(mat)
        while n - 2 * count > 0:
            for i in range((n - 1) - 2 * count):
                temp = mat[count][i + count]
                mat[count][i + count] = mat[((n - 1) - i) - count][count]
                mat[((n - 1) - i) - count][count] = mat[(n - 1) - count][((n - 1) - i) - count]
                mat[(n - 1) - count][((n - 1) - i) - count] = mat[i + count][(n - 1) - count]
                mat[i + count][(n - 1) - count] = temp
            count += 1