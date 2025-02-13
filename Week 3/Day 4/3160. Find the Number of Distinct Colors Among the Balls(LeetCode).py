# February 13 2025
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ind = {}
        freq = {}
        res = []
        for q in queries:
            if q[0] in ind:
                c = ind[q[0]]
                freq[c] -= 1
                if freq[c] == 0:
                    freq.pop(c)
            ind[q[0]] = q[1]
            c = q[1]
            freq[c] = freq.get(c, 0) + 1
            res.append(len(freq))
        return res


