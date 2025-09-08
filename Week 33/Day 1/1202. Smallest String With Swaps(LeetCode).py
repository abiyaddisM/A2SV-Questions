# September 8 2025
# https://leetcode.com/problems/smallest-string-with-swaps/description/
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        def find(x):
            if parent[x] == x:
                return x
            temp = find(parent[x])
            parent[x] = temp
            return temp
        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                parent[t2] = t1
        for p in pairs:
            union(p[0], p[1])

        dic = defaultdict(deque)
        for i in range(len(parent)):
            p = find(parent[i])
            dic[p].append(s[i])
        for k, v in dic.items():
            v = deque(sorted(v))
            dic[k] = v
        res = []
        for i in range(len(parent)):
            p = find(parent[i])
            res.append(dic[p].popleft())
        return ''.join(res)