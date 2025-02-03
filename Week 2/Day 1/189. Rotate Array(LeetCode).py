#February 3 2025
#https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        replaceVal = nums[0]
        replaceInd = 0
        myset = set()
        for _ in range(len(nums)):
            if replaceInd in myset:
                replaceInd += 1
                replaceVal = nums[(replaceInd) % len(nums)]
            nextInd = (replaceInd + k) % len(nums)

            nums[nextInd], replaceVal = replaceVal, nums[nextInd]
            myset.add(replaceInd)
            replaceInd = nextInd
