# February 11 2025
# https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for k, v in freq.items():
            if v <= len(nums) // 3:
                continue
            res.append(k)
        return res
