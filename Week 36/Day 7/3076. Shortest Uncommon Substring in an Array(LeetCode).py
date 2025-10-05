# October 5 2025
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        sub_map = defaultdict(set)

        for i, word in enumerate(arr):
            n = len(word)
            for l in range(1, n + 1):
                for j in range(n - l + 1):
                    sub = word[j:j + l]
                    sub_map[sub].add(i)

        res = []
        for i, word in enumerate(arr):
            candidates = []
            n = len(word)
            for l in range(1, n + 1):
                for j in range(n - l + 1):
                    sub = word[j:j + l]
                    if sub_map[sub] == {i}:
                        candidates.append(sub)
                if candidates:
                    break

            if candidates:
                res.append(min(candidates))
            else:
                res.append("")
        return res
