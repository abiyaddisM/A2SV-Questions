# October 4 2025
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path
from typing import List
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        row, col = len(grid), len(grid[0])

        dis = [[float('inf') for _ in range(col)] for _ in range(row)]
        dis[0][0] = grid[0][0]

        if dis[0][0] >= health:
            return False

        heap = [(dis[0][0], (0, 0))]
        while heap:
            curDis, (i, j) = heapq.heappop(heap)
            if curDis > dis[i][j]:
                continue

            if curDis >= health:
                continue

            if i == row - 1 and j == col - 1:
                return True

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nextX = i + dx
                nextY = j + dy
                if not (0 <= nextX < row and 0 <= nextY < col):
                    continue
                newDis = curDis + grid[nextX][nextY]
                if dis[nextX][nextY] > newDis:
                    dis[nextX][nextY] = newDis
                    heapq.heappush(heap, (newDis, (nextX, nextY)))

        return False
