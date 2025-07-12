# July 11 2025
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        heap = []
        for i in range(n):
            heapq.heappush(heap, (mat[i][0], i, 0))
        count = 1
        while heap:
            val, i, j = heapq.heappop(heap)
            if count == k:
                return val
            if j != n - 1:
                heapq.heappush(heap, (mat[i][j + 1],  i, j + 1))
            count += 1