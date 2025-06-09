# June 9 2025
# https://leetcode.com/problems/additive-number/description/

class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        def check(num):
            return not (len(num) > 1 and num[0] == '0')
        def helper(total, pre, index, count):
            if index == len(nums):
                return count > 2
            for i in range(index, len(nums)):
                temp = int(nums[index: i + 1])
                print(temp,total,i)
                if temp == total and check(nums[index: i + 1]):
                    if helper(temp + pre, temp, i + 1, count + 1):
                        return True
            return False

        for i in range(1,len(nums)):
            for j in range(i + 1, len(nums)):
                l = nums[0:i]
                r = nums[i:j]
                if not check(l) or not check(r):
                    continue
                l = int(l)
                r = int(r)
                if helper(l + r, r, j, 2):
                    return True
        return False