# October 3 2025
# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for r in roads:
            graph[r[0]].append((r[1], r[2]))
            graph[r[1]].append((r[0], r[2]))

        distance = [float('inf')] * n
        distance[0] = 0
        freq = [0] * n
        freq[0] = 1

        heap = [(0, 0)]
        while heap:
            curDis, curInd = heapq.heappop(heap)
            if curDis > distance[curInd]:
                continue

            for nextInd, nextDis in graph[curInd]:
                newDis = curDis + nextDis

                if newDis < distance[nextInd]:
                    distance[nextInd] = newDis
                    freq[nextInd] = freq[curInd]
                    heapq.heappush(heap, (newDis, nextInd))

                elif newDis == distance[nextInd]:
                    freq[nextInd] = (freq[nextInd] + freq[curInd]) % MOD

        return freq[n - 1] % MOD
