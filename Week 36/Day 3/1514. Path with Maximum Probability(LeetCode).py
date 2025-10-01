# October 1 2025
# https://leetcode.com/problems/path-with-maximum-probability/description/
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = [0.0] * n
        prob[start_node] = 1.0

        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob

            for nei, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[nei]:
                    prob[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0
