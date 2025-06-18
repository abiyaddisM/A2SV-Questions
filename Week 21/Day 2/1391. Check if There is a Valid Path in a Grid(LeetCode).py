# June 17 2025
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dic = {
            1 : [(0, 1), (0, -1)],
            2 : [(1, 0), (-1, 0)],
            3 : [(0, -1), (1, 0)],
            4 : [(0, 1), (1, 0)],
            5 : [(0, -1), (-1, 0)],
            6 : [(0, 1), (-1, 0)]

        }
        visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def helper(grid, visited, row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            visited[row][col] = True

            for rc, cc in dic[grid[row][col]]:
                nr = row + rc
                nc = col + cc
                if not inbound(nr, nc) or visited[nr][nc]:
                    continue
                for rc2, cc2 in dic[grid[nr][nc]]:
                    nr2 = nr + rc2
                    nc2 = nc + cc2
                    if row == nr2 and col == nc2:
                        if helper(grid, visited, nr, nc):
                            return True
            return False
        return helper(grid, visited, 0, 0)