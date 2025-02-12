# February 11 2025
# https://leetcode.com/problems/replace-elements-in-an-array/
class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        pos = {}
        for i in range(len(nums)):
            pos[nums[i]] = i

        for o in op:
            nums[pos[o[0]]] = o[1]
            pos[o[1]] = pos[o[0]]
            del pos[o[0]]
        return nums