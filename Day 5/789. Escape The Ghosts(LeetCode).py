#January 31 2025
#https://leetcode.com/problems/escape-the-ghosts/
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], t: List[int]) -> bool:
        total = abs(t[0]) + abs(t[1])
        for a in ghosts:
            gTotal = abs(a[0] - t[0]) + abs(a[1] - t[1])
            if gTotal <= total:
                return False
        return True
