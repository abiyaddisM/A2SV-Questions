# July 14 2025
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, n1: List[int], n2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []
        v = set()
        heapq.heappush(heap, (n1 + n2, 0, 0))
        v.add((0, 0))
        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append([n1[i], n2[j]])
            if i + 1 < len(n1) and (i + 1, j) not in v:
                v.add((i + 1, j))
                heapq.heappush(heap, (n1[i + 1] + n2[j], i + 1, j))
            if j + 1 < len(n2) and (i, j + 1) not in v:
                v.add((i, j + 1))
                heapq.heappush(heap, (n1[i] + n2[j + 1], i, j + 1))
        return res