# February 9 2025
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/
class Solution:
    def findIndices(self, nums: List[int], iD: int, vD: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j - i >= iD and abs(nums[j] - nums[i]) >= vD:
                    return [i, j]

        return [-1, -1]