#January 31 2025
#https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            tRes = []
            x = nums[i]
            while x >= 1:
                tRes.append(x % 10)
                x //= 10
            res.extend(tRes[::-1])
        return res

