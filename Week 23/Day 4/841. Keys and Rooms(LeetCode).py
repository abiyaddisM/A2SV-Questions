# July 3 2025
# https://leetcode.com/u/abiymw17/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        que = deque(rooms[0])
        while que:
            pop = que.popleft()
            visited[pop] = True
            for r in rooms[pop]:
                if not visited[r]:
                    que.append(r)

        for i in range(1, len(visited)):
            if not visited[i]:
                return False
        return True