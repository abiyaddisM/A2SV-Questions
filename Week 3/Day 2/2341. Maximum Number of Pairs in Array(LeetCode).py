# February 11 2025
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pair = 0
        left = 0
        for k, v in freq.items():
            pair += v // 2
            if v % 2 == 1:
                left += 1

        return [pair, left]