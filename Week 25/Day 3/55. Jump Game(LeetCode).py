# July 16 2025
# https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        start = nums[0] - 1
        for i in range(1, len(nums) - 1):
            if nums[i] == 0 and start == 0:
                return False
            start = max(start, nums[i])
            start -= 1
        return True
