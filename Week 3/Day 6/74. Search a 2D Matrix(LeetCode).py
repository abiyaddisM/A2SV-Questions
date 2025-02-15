# February 15 2025
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lefti, leftj = 0, 0
        righti, rightj = len(matrix) - 1, len(matrix[0]) - 1
        while lefti < righti:
            middle = (lefti + righti) // 2
            if matrix[middle][0] > target:
                righti = middle - 1
            elif matrix[middle][-1] < target:
                lefti = middle + 1
            elif matrix[middle][0] <= target <= matrix[middle][-1]:
                lefti = middle
                righti = middle
        while leftj <= rightj:
            middle = (leftj + rightj) // 2
            if matrix[lefti][middle] == target:
                return True
            elif matrix[lefti][middle] > target:
                rightj = middle - 1
            else:
                leftj = middle + 1
        return False