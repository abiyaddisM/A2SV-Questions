# April 4 2025
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        res = []
        heap = []
        maxs = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0],i, 0))
            maxs = max(maxs, nums[i][0])

        while True:
            mins, i, j = heapq.heappop(heap)
            if len(res) == 0 or res[1] - res[0] > maxs - mins:
                res = [mins, maxs]
            j += 1
            if len(nums[i]) <= j :
                break
            heapq.heappush(heap, (nums[i][j],i, j))
            maxs = max(maxs, nums[i][j])
        return res