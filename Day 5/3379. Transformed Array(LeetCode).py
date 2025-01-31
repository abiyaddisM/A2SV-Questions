#January 31 2025
#https://leetcode.com/problems/transformed-array/
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            s = i
            if nums[i] > 0:
                s = (i + nums[i]) % len(nums)
            elif nums[i] < 0:
                s = (i + nums[i]) % len(nums)
            res.append(nums[s])
            print(s)
        return res
