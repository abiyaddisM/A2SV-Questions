# July 10 2025
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        temp = 0
        for i in range(k):
            temp = heapq.heappop(nums)
        return -temp