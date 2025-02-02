#January 30 2025
#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = length - 1
            while l < r:

                if l != i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r != length - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1

        return res