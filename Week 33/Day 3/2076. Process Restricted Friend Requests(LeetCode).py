# September 10 2025
# https://leetcode.com/problems/process-restricted-friend-requests/description/
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]

        rest = [set() for _ in range(n)]
        for a, b in restrictions:
            rest[a].add(b)
            rest[b].add(a)

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> int:
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            if rank[ra] == rank[rb]:
                parent[ra] = rb
                rank[rb] += 1
                if len(rest[rb]) < len(rest[ra]):
                    rest[rb], rest[ra] = rest[ra], rest[rb]
                rest[rb] |= rest[ra]
                rest[ra].clear()
                return rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
                if len(rest[ra]) < len(rest[rb]):
                    rest[ra], rest[rb] = rest[rb], rest[ra]
                rest[ra] |= rest[rb]
                rest[rb].clear()
                return ra
            else:
                parent[ra] = rb
                if len(rest[rb]) < len(rest[ra]):
                    rest[rb], rest[ra] = rest[ra], rest[rb]
                rest[rb] |= rest[ra]
                rest[ra].clear()
                return rb

        res = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            if ru == rv:
                res.append(True)
                continue

            conflict = False
            for x in rest[ru]:
                if find(x) == rv:
                    conflict = True
                    break
            if not conflict:
                for x in rest[rv]:
                    if find(x) == ru:
                        conflict = True
                        break

            if conflict:
                res.append(False)
            else:
                union(ru, rv)
                res.append(True)

        return res
