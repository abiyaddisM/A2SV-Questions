# August 27 2025
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        out = []
        for ch in baseStr:
            idx = ord(ch) - ord('a')
            rep = find(idx)
            out.append(chr(rep + ord('a')))
        return ''.join(out)
