#Febuary 2 2025
#https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        state = False
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                state = True
            else:
                if state:
                    break
        return res
