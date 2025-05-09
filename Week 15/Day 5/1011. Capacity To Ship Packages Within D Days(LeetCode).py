# May 9 2025
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/1629601019/
class Solution:
    def shipWithinDays(self, we: List[int], days: int) -> int:
        def helper(m):
            count = 1
            total = 0
            for i in range(len(we)):
                if total + we[i] > m:
                    count += 1
                    total = 0
                total += we[i]

            return count <= days

        l = max(we)
        r = sum(we)
        while l <= r:
            m = (r + l) // 2
            if helper(m):
                r = m - 1
            else:
                l = m + 1

        return l
