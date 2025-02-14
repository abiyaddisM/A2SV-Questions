# February 13 2025
# https://leetcode.com/problems/increasing-triplet-subsequence/description/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        val1 = 2**31
        val2 = 2**31
        for n in nums:
            if n <= val1:
                val1 = n
            elif n <= val2:
                val2 = n
            else:
                return True
        return False