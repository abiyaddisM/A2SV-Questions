# March 6 2025
# https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, pt: List[int], tasks: List[int]) -> int:
        pt.sort()
        tasks.sort(reverse = True)
        res = 0
        for i in range(len(pt)):
            j = 4 * i
            res = max(pt[i] + tasks[j],res)
        return res