# July 18 2025
# https://leetcode.com/problems/non-overlapping-intervals/description/
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        res = 0
        for i in range(1,len(intervals)):
            if prev[1] > intervals[i][0]:
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
                res += 1
                continue
            prev = intervals[i]
        return res