# May 15 2025
# https://leetcode.com/problems/magnetic-force-between-two-balls/description/
class Solution:
    def maxDistance(self, pos: List[int], k: int) -> int:
        pos.sort()
        def helper(m):
            count = 1
            pre = pos[0]
            for i in range(1,len(pos)):
                if pos[i] - pre >= m:
                    count += 1
                    pre = pos[i]
            return count >= k
        l = 0
        r = pos[-1]
        res = 0
        while l <= r:
            m = (r + l) // 2
            if helper(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res