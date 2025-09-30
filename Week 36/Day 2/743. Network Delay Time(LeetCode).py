# September 30 2025
# https://leetcode.com/problems/network-delay-time/description/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for t in times:
            graph[t[0] - 1].append((t[1] - 1, t[2]))

        delay = [float('inf') for _ in range(n)]
        delay[k - 1] = 0
        heap = [(0, k - 1)]
        while heap:
            cost, cur = heapq.heappop(heap)
            if cost > delay[cur]:
                continue
            delay[cur] = cost
            for nei, weight in graph[cur]:
                if delay[nei] == float('inf'):
                    heapq.heappush(heap, (weight + cost, nei))
        res = max(delay)

        return -1 if res == float('inf') else res