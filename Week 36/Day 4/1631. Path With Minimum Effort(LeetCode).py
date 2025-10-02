# October 2 2025
# https://leetcode.com/problems/path-with-minimum-effort/description/
class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        row, col = len(h), len(h[0])
        dis = [ [float('inf')] * col for _ in range(row)]
        visited = [ [False] * col for _ in range(row)]
        heap = [(0, (0, 0))]
        dis[0][0] = 0
        while heap:
            w, cur = heapq.heappop(heap)
            i, j = cur
            visited[i][j] = True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = dx + i
                ny = dy + j
                if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                    temp = max(w, abs(h[i][j] - h[nx][ny]))
                    if dis[nx][ny] > temp :
                        dis[nx][ny] = temp
                        heapq.heappush(heap, (temp, (nx, ny)))
        return dis[-1][-1]