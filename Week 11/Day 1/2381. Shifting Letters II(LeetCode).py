# April 7 2025
# https://leetcode.com/problems/shifting-letters-ii/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums = [0 for i in range(len(s) + 1)]
        for sh in shifts:
            nums[sh[0]] += 1 if sh[2] == 1 else -1
            nums[sh[1] + 1] += -1 if sh[2] == 1 else 1

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        res = ''
        for i in range(len(s)):
            res += chr((ord(s[i]) - 97 + nums[i]) % 26 + 97)

        return res
