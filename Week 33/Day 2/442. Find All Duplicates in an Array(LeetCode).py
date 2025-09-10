# September 9 2025
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ms = set()
        res = []
        for n in nums:
            if n in ms:
                res.append(n)
            ms.add(n)
        return res