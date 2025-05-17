# May 16 2025
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
from typing import List

class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:
        if m * k > len(bd):
            return -1

        def helper(day):
            count = 0
            a = 0
            for i in range(len(bd)):
                if bd[i] <= day:
                    a += 1
                else:
                    a = 0
                if a == k:
                    a = 0
                    count += 1
            return count >= m

        l = 0
        r = max(bd)
        res = -1
        while l <= r:
            mid = (r + l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
