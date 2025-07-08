# July 9 2025
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = [-n for n in piles]  # Negate all numbers
        heapq.heapify(nums)
        for i in range(k):
            temp = -heapq.heappop(nums)
            heapq.heappush(nums, -math.ceil(temp/2))
        return sum([-n for n in nums])