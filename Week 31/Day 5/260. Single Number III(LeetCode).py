# August 29 2025
# https://leetcode.com/problems/single-number-iii/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = 0
        for x in nums:
            temp ^= x
        mask = temp & -temp

        t1 = 0
        t2 = 0
        for x in nums:
            if x & mask:
                t1 ^= x
            else:
                t2 ^= x

        return [t1, t2]