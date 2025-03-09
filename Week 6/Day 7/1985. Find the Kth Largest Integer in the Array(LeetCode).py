# March 9 2025
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(reverse = True,key = lambda x:int(x))
        return nums[k - 1]