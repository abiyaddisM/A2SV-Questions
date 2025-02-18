# February 18 2025
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i + 1 for i in range(n)]
        i = 0
        while len(nums) > 1:
            i = ((k - 1) + i) % len(nums)
            nums.pop(i)
            print(i)
        return nums[0]